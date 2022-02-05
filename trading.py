import ccxt
import pandas as pd
from binance.client import Client
from binance import Binance

binance = ccxt.binance()
markets = binance.load_markets()              #마켓 조회    (딕셔너리)
btc = binance.fetch_ticker("BTC/USDT")        #현재가 조회  (딕셔너리)
btc_ohlcv = binance.fetch_ohlcv("BTC/USDT")   #분봉 조회

df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'voluem'])
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index('datetime', inplace=True)

print(df)