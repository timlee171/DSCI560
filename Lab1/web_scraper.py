from bs4 import BeautifulSoup
from selenium import webdriver
import requests

driver = webdriver.Chrome()
URL =  "https://www.cnbc.com/world/?region=world"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

result = soup.find_all("a",class_= "MarketCard-container")
print(result.content)
#with open('web_data.html', 'w', encoding='utf-8') as file:
#	file.write(str(result))
#print('saved output as html file')
