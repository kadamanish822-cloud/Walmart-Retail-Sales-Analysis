-- PostgreSQL schema matching the supplied dataset.
CREATE TABLE walmart_sales (
    invoice_id BIGINT,
    branch TEXT,
    city TEXT,
    category TEXT,
    unit_price NUMERIC(12,2),
    quantity NUMERIC(12,2),
    date DATE,
    time TEXT,
    payment_method TEXT,
    rating NUMERIC(4,2),
    profit_margin NUMERIC(8,4),
    revenue NUMERIC(14,2),
    gross_profit_estimate NUMERIC(14,2)
);
