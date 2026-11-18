"""Walmart Retail Analytics pipeline.
Run from project root: python src/analysis.py
"""
from pathlib import Path
import re, json
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "Walmart.csv"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "outputs" / "figures"
REPORTS = ROOT / "reports"

def main():
    if not RAW.exists():
        raise FileNotFoundError("Put Walmart.csv in data/raw/")
    df = pd.read_csv(RAW)
    df.columns = [re.sub(r"[^a-z0-9]+", "_", str(c).strip().lower()).strip("_") for c in df.columns]
    df["unit_price"] = pd.to_numeric(df["unit_price"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False), errors="coerce")
    for c in ["quantity", "rating", "profit_margin"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    duplicate_rows = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()
    df["revenue"] = df["unit_price"] * df["quantity"]
    df["estimated_profit"] = df["revenue"] * df["profit_margin"]
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.month_name()
    df["day_name"] = df["date"].dt.day_name()
    df["hour"] = pd.to_datetime(df["time"], format="%H:%M:%S", errors="coerce").dt.hour
    PROCESSED.mkdir(parents=True, exist_ok=True); FIGURES.mkdir(parents=True, exist_ok=True); REPORTS.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / "walmart_cleaned_all_rows.csv", index=False)
    valid = df.dropna(subset=["revenue"]).copy()
    valid.to_csv(PROCESSED / "walmart_revenue_analysis.csv", index=False)
    metrics = {
      "input_rows": int(len(pd.read_csv(RAW))), "rows_after_deduplication": int(len(df)),
      "exact_duplicate_rows_removed": duplicate_rows, "revenue_eligible_rows": int(len(valid)),
      "total_revenue": round(float(valid.revenue.sum()), 2),
      "estimated_gross_profit": round(float(valid.estimated_profit.sum()), 2),
      "average_transaction_revenue": round(float(valid.revenue.mean()), 2),
      "units_sold": round(float(valid.quantity.sum()), 0),
      "average_rating": round(float(df.rating.mean()), 2),
      "date_min": str(df.date.min().date()), "date_max": str(df.date.max().date())
    }
    (REPORTS / "key_metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    category = valid.groupby("category").revenue.sum().sort_values(ascending=False)
    branch = valid.groupby("branch").revenue.sum().sort_values(ascending=False)
    payment = valid.payment_method.value_counts()
    for values, title, filename, horizontal in [
        (category, "Revenue by Product Category", "revenue_by_category.png", True),
        (branch.head(10), "Top 10 Branches by Revenue", "top_10_branches.png", True),
        (payment, "Transactions by Payment Method", "payment_methods.png", False),
        (valid.groupby("year").revenue.sum(), "Revenue by Year", "revenue_by_year.png", False),
        (valid.groupby(valid.date.dt.to_period("M")).revenue.sum(), "Monthly Revenue Trend", "monthly_revenue_trend.png", False),
        (valid.groupby("hour").revenue.sum(), "Revenue by Hour of Day", "revenue_by_hour.png", False)
    ]:
        plt.figure(figsize=(10,5))
        (values.sort_values() if horizontal else values).plot(kind="barh" if horizontal else ("line" if "Monthly" in title else "bar"))
        plt.title(title); plt.ylabel("Revenue / Transactions"); plt.tight_layout(); plt.savefig(FIGURES / filename, dpi=160); plt.close()
    print(json.dumps(metrics, indent=2))
    print("Pipeline completed. Review outputs/figures and reports/ before publishing.")

if __name__ == "__main__":
    main()
