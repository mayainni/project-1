CREATE TABLE prices(
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    price NUMERIC(20, 8) NOT NULL,
    volume NUMERIC(20, 8),
    fetched_at TIMESTAMP NOT NULL DEFAULT NOW()
);