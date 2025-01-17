# Name: Tsung Ting Lee
# USC ID: 3505261806
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests

service = Service("/home/tsung-ting-lee/Downloads/chromedriver-linux64/chromedriver")
URL =  "https://www.cnbc.com/world/?region=world"
driver = webdriver.Chrome(service = service) 
driver.get(URL)
soup = BeautifulSoup(driver.page_source, "html.parser")

result = soup.find_all(class_= [ "MarketsBanner-main", "LatestNews-isHomePage"])
with open('../data/raw_data/web_data.html', 'w', encoding='utf-8') as file:
	file.write(str(result))
print('saved output as html file')
