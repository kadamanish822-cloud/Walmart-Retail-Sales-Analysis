-- PostgreSQL table matching the supplied Walmart.csv columns.
CREATE TABLE IF NOT EXISTS walmart_sales (
    invoice_id BIGINT,
    branch VARCHAR(20),
    city VARCHAR(100),
    category VARCHAR(100),
    unit_price NUMERIC(12,2),
    quantity INTEGER,
    date DATE,
    time TIME,
    payment_method VARCHAR(30),
    rating NUMERIC(4,2),
    profit_margin NUMERIC(6,4),
    revenue NUMERIC(14,2),
    estimated_profit NUMERIC(14,2)
);
