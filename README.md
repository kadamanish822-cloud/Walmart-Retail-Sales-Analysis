# Walmart Retail Sales Analysis

An end-to-end retail analytics project built from the supplied Walmart CSV dataset using **Python, Pandas, Matplotlib and SQL**.

## Project objective
Analyze retail transaction data to understand revenue performance, product-category contribution, branch performance, payment-method usage, customer ratings and time trends.

## Dataset
- Source repository: https://github.com/jay51211/Walmart-Data-Analysis
- Original CSV: `data/raw/Walmart.csv`
- Dataset contains 10,051 rows and 11 columns before cleaning.
- Date coverage after parsing: 2019-01-01 to 2023-12-31.
- The supplied file contains invoice ID, branch, city, category, unit price, quantity, date, time, payment method, rating and profit margin.

## Key findings (calculated from the supplied CSV)
- **10,051** input rows; **51** exact duplicate rows removed, leaving **10,000** rows.
- **9,969** rows have sufficient price and quantity data for revenue analysis.
- Total calculated revenue: **$1,209,726.38**.
- Estimated gross profit: **$476,139.43**, calculated as revenue × provided profit margin.
- Average transaction revenue: **$121.35**.
- Units sold: **23,483**.
- Average customer rating: **5.83**.
- Highest revenue category: **Fashion accessories** ($489,480.90).
- Highest revenue branch: **WALM009** ($25,688.34).
- Highest revenue city: **Weslaco** ($46,351.79).
- Most frequently used payment method: **Credit card** (4,256 revenue-eligible transactions).
- Highest revenue year: **2019** ($307,587.38).

## Data cleaning decisions
1. Standardized column names to lowercase.
2. Converted `unit_price` from currency text to numeric.
3. Parsed dates using day-first interpretation, consistent with dates such as `22/08/21`.
4. Removed 51 exact duplicate rows.
5. Created `revenue = unit_price × quantity`.
6. Created `estimated_profit = revenue × profit_margin`.
7. Added year, month, month name, weekday and hour features.
8. Retained rows with missing financial inputs in `walmart_cleaned_all_rows.csv`, but excluded them from revenue calculations. There are 31 rows with missing unit price (and corresponding quantity).

## Repository structure
```text
Walmart_Retail_Analytics_Project/
├── data/
│   ├── raw/Walmart.csv
│   └── processed/
│       ├── walmart_cleaned_all_rows.csv
│       └── walmart_revenue_analysis.csv
├── notebooks/Walmart_Retail_Analysis.ipynb
├── src/analysis.py
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
├── outputs/figures/
├── reports/
│   ├── key_metrics.json
│   ├── category_performance.csv
│   └── branch_performance.csv
├── requirements.txt
└── README.md
```

## Run the project
### 1. Create environment
```bash
python -m venv .venv
```
Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run analysis
```bash
python src/analysis.py
```
### 4. Explore notebook
Open `notebooks/Walmart_Retail_Analysis.ipynb` in Jupyter Notebook or VS Code and run all cells.

## SQL analysis
Use `sql/schema.sql` to create a PostgreSQL table. Import `data/processed/walmart_revenue_analysis.csv` into the table, then execute `sql/analysis_queries.sql`. The CSV already contains calculated `revenue` and `estimated_profit` columns.

## Business recommendations
- Prioritize stock and merchandising reviews for Fashion accessories and Home and lifestyle, the two largest revenue categories in this dataset.
- Compare branch-level category mix and customer ratings before making inventory decisions.
- Investigate the missing financial fields at source; avoid inventing prices or quantities.
- Track revenue, units, average rating and estimated profit together rather than relying on revenue alone.

## Limitations
- Revenue is calculated from unit price × quantity; it is not an independently supplied total field.
- Estimated profit uses the dataset's supplied profit margin; it is not audited accounting profit.
- Rows missing price/quantity are excluded from revenue and profit totals.
- This dataset is a sample for portfolio analysis; findings should not be generalized to all Walmart operations.

## Attribution
Dataset source: [jay51211/Walmart-Data-Analysis](https://github.com/jay51211/Walmart-Data-Analysis). This repository is an independent learning/portfolio analysis of that dataset. Retain attribution to the original data source.
