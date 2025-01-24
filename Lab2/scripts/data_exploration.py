# Name: Tsung Ting Lee
# USC ID: 3505261806

import yfinance as yf
import pandas as pd
from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pdfplumber
import pytesseract

#stock = "TSLA"
#stock_data = yf.download(stock, start="2023-01-01", end="2025-01-01")

#service = Service("/home/tsung-ting-lee/Downloads/chromedriver-linux64/chromedriver")
#URL = ""
#driver = webdriver.Chrome(service = service)
#driver.get(URL)
#soup = BeautifulSoup(driver.page_source, 'html.parser')


#$stock_data.to_csv('../data/raw_data/stock_data.csv', index=False)
#print('saved data as csv file')

with pdfplumber.open("../data/raw_data/tsla-20241023-gen.pdf") as pdf:
	page_28 = pdf.pages[28]
	texts = page_28.extract_text()

#lines = texts.strip('/n')
data = []
for text in texts:
	data.append(text)

df = pd.DataFrame(data)
df.to_csv("../data/raw_data/tsla_financial_report.csv", index=False)
print('saved data as csv file')
