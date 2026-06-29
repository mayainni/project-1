from BD_connect import conn
import ccxt
import time

##
exchenge = ccxt.bybit()

##
curr = conn.cursor()

##
while True:
    try:
        ticker = exchenge.fetch_ticker('BTC/USDT')
        curr.execute(
            "INSERT INTO prices (symbol, price, volume) VALUES (%s, %s, %s)",
            (ticker['symbol'], ticker['last'], ticker['baseVolume']))
        conn.commit()
        print(f"Записано: {ticker['symbol']} = {ticker['last']}")
    except Exception as e:
        print(f"Ошибка: {e}")
    time.sleep(60)
