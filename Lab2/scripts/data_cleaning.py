import pandas as pd
import csv

web_data = pd.read_csv("../data/raw_data/web_data.csv")
stock_data = pd.read_csv("../data/raw_data/stock_data.csv")
house_price_data = pd.read_csv("../data/raw_data/la_house_price.csv")

print(web_data.isnull().sum())
print(stock_data.isnull().sum())
print(house_price_data.isnull().sum())

web_data = web_data.dropna()
stock_data = stock_data.dropna()
house_price_data = house_price_data.dropna()

print("web_data shape: ", web_data.shape)
print("stock data shape: ", stock_data.shape)
print("house data shape: ", house_price_data.shape)

web_data.to_csv("../data/processed_data/cleaned_web_data.csv", index = False)
stock_data.to_csv("../data/processed_data/cleaned_stock_data.csv", index = False)
house_price_data.to_csv("../data/processed_data/clean_stock_data.csv", index = False)

print("file is saved")
