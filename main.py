import psycopg2
import ccxt
import time

##
exchenge = ccxt.bybit()
ticker = exchenge.fetch_ticker('BTC/USDT')

##
conn = psycopg2.connect(
    host='localhost',
    dbname='crypto_data',
    user='postgres',
    password='makar',
    port=5432
)
curr = conn.cursor()

##
while True:
    try:
        curr.execute(
            "INSERT INTO prices (symbol, price, volume) VALUES (%s, %s, %s)",
            (ticker['symbol'], ticker['last'], ticker['baseVolume']))
        conn.commit()
        print(f"Записано: {ticker['symbol']} = {ticker['last']}")
    except Exception as e:
        print(f"Ошибка: {e}")
    time.sleep(60)
