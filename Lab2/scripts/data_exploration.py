import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pdfplumber
import pytesseract

stock = "TSLA"
stock_data = yf.download(stock, start="2023-01-01", end="2025-01-01")

stock_data.to_csv('../data/raw_data/stock_data.csv', index=False)
print('saved data as csv file')
