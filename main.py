import BD_connect
import ccxt
import time
import random

## Получение массива данных крипты
exchenge = ccxt.bybit()

## Подключение к БД
curr = BD_connect.conn.cursor()

## Функция, которая заносит из массива в таблицу каждые 5-60 секунд
while True:
    try:
        ticker = exchenge.fetch_ticker('BTC/USDT')
        curr.execute(
            "INSERT INTO prices (symbol, price, volume) VALUES (%s, %s, %s)",
            (ticker['symbol'], ticker['last'], ticker['baseVolume']))
        BD_connect.conn.commit()
        print(f"Записано: {ticker['symbol']} = {ticker['last']}")
    except Exception as e:
        print(f"Ошибка: {e}")
    time.sleep(random.randrange(5,60,5))
