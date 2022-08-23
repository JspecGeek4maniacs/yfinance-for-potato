import yfinance as yf
import matplotlib.pyplot as plt

data=yf.download('ETH-USD')
data.plot()
