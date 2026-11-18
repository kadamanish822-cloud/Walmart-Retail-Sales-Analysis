-- Import data/processed/walmart_revenue_analysis.csv into walmart_sales.
-- The CSV has revenue and estimated_profit calculated in Python.

-- 1. KPI overview
SELECT COUNT(*) AS transactions,
       ROUND(SUM(revenue),2) AS total_revenue,
       ROUND(AVG(revenue),2) AS avg_transaction_revenue,
       SUM(quantity) AS units_sold,
       ROUND(AVG(rating),2) AS average_rating
FROM walmart_sales;

-- 2. Revenue by product category
SELECT category, SUM(quantity) AS units_sold,
       ROUND(SUM(revenue),2) AS revenue,
       ROUND(AVG(rating),2) AS average_rating
FROM walmart_sales
GROUP BY category ORDER BY revenue DESC;

-- 3. Top 10 branches
SELECT branch, city, ROUND(SUM(revenue),2) AS revenue
FROM walmart_sales
GROUP BY branch, city ORDER BY revenue DESC LIMIT 10;

-- 4. Payment method mix
SELECT payment_method, COUNT(*) AS transactions,
       ROUND(100.0*COUNT(*)/SUM(COUNT(*)) OVER (),2) AS transaction_share_pct
FROM walmart_sales GROUP BY payment_method ORDER BY transactions DESC;

-- 5. Yearly sales trend
SELECT EXTRACT(YEAR FROM date) AS sales_year,
       ROUND(SUM(revenue),2) AS revenue
FROM walmart_sales GROUP BY sales_year ORDER BY sales_year;

-- 6. Monthly trend
SELECT DATE_TRUNC('month', date)::date AS sales_month,
       ROUND(SUM(revenue),2) AS revenue
FROM walmart_sales GROUP BY sales_month ORDER BY sales_month;

-- 7. Hourly sales
SELECT EXTRACT(HOUR FROM time) AS sales_hour,
       ROUND(SUM(revenue),2) AS revenue
FROM walmart_sales GROUP BY sales_hour ORDER BY sales_hour;

-- 8. Profit estimate by category
SELECT category, ROUND(SUM(estimated_profit),2) AS estimated_profit,
       ROUND(AVG(profit_margin)*100,2) AS average_margin_pct
FROM walmart_sales GROUP BY category ORDER BY estimated_profit DESC;
