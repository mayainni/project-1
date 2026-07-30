import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='crypto_data',
    user='postgres',
    password='makar',
    port=5432
)