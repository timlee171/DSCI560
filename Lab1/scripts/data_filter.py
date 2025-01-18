# Name: Tsung Ting Lee
# USC ID: 3505261806

from bs4 import BeautifulSoup 
import csv

with open('../data/raw_data/web_data.html', 'r') as file:
	content = file.read()

soup = BeautifulSoup(content, 'html.parser')

marketCard_symbol = []
marketCard_stockPosition = []
marketCard_changePct = []
latestNews_timestamp = []
latestNews_title = []
latestNews_link = []

for marketbanner in soup.find_all(class_= "MarketCard-container"):
	symbol = marketbanner.find(class_="MarketCard-symbol")
	stockPosition = marketbanner.find(class_="MarketCard-stockPosition")
	changePct = marketbanner.find(class_="MarketCard-changesPct")
	marketCard_symbol.append(symbol.text)
	marketCard_stockPosition.append(stockPosition.text)
	marketCard_changePct.append(changePct.text)
for latestnew in soup.find_all(class_="LatestNews-item"):
	timestamp = latestnew.find(class_="LatestNews-timestamp")
	title = latestnew.find(class_="LatestNews-headline")
	link = latestnew.find(class_="LatestNews-headline").get('href')
	latestNews_timestamp.append(timestamp.text)
	latestNews_title.append(title.text)
	latestNews_link.append(link)
print(marketCard_symbol)
print(marketCard_stockPosition)
print(marketCard_changePct)
print(latestNews_timestamp)
print(latestNews_title)
print(latestNews_link)


market_header = ["marketCard_symbol","marketCard_stockPosition","marketCard_changePct"]
news_header = ["latestNews_timestamp","latestNews_title","latestNews_link"]
market_data = zip(marketCard_symbol, marketCard_stockPosition, marketCard_changePct)
news_data = zip(latestNews_timestamp,latestNews_title,latestNews_link)

with open("../data/processed_data/market_data.csv", "w", newline="") as output1:
        writer = csv.writer(output1)
        writer.writerow(market_header)
        writer.writerows(market_data)

with open("../data/processed_data/news_data.csv", "w", newline="") as output2:
	writer = csv.writer(output2)
	writer.writerow(news_header)
	writer.writerows(news_data)

print("file is created")
