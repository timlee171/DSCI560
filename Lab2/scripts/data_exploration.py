# Name: Tsung Ting Lee
# USC ID: 3505261806

import yfinance as yf
import pandas as pd
from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pdfplumber
import pytesseract
import csv

stock = "TSLA"
stock_data = yf.download(stock, start="2023-01-01", end="2025-01-01")

service = Service("/home/tsung-ting-lee/Downloads/chromedriver-linux64/chromedriver")
URL = "https://www.amazon.com/s?k=headphones&i=electronics&crid=37FKIKE4ZG1PF&sprefix=headphone%2Celectronics%2C200&ref=nb_sb_noss_2"
driver = webdriver.Chrome(service = service)
driver.get(URL)
soup = BeautifulSoup(driver.page_source, 'html.parser')

products = []
prices = []
for result in soup.find_all(class_=["puisg-col-inner","a-size-medium a-spacing-none a-color-base a-text-normal"]):
	product = result.get("aria-label")
	products.append(product)
for result2 in soup.find_all(class_=["puisg-col-inner","a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal"]):
	price = result2.find(class_="a-offscreen")
	if price:
		prices.append(price.text)
	else:
		prices.append("nan") 

header = ["product","price"]
product_data =zip(products, prices)

with open("../data/raw_data/web_data.csv", "w") as output:
	writer = csv.writer(output)
	writer.writerow(header)
	writer.writerows(product_data)
print("file is created")

stock_data.to_csv('../data/raw_data/stock_data.csv', index=False)
print('saved data as csv file')

with pdfplumber.open("../data/raw_data/Los-Angeles-County-January-2024-Market-Report.pdf") as pdf:
	page_11 = pdf.pages[10]
	table = page_11.extract_table()

df = pd.DataFrame(table)
df.columns = ["Study Area","Rating", "Median/Rental Parity", "% Rental Parity", "Historic Premium", "% Historic Prem"]
df.to_csv("../data/raw_data/la_house_price.csv", index=False)
print('saved house price data as csv file')

