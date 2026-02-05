# batch-data-pipeline-sales-analytics
---

## 📊 Analytics Reports

After running the ETL pipeline, the following analytics outputs are generated:

1. **Total Revenue by Country**  
   - Sum of `total_price` for each country.
   - Example:

| country | total_revenue |
|---------|---------------|
| Canada  | 96.0          |
| India   | 110.0         |
| USA     | 166.0         |

2. **Total Quantity by Country**  
   - Total items sold per country.
   - Example:

| country | quantity |
|---------|---------|
| Canada  | 8       |
| India   | 5       |
| USA     | 15      |

3. **Top 5 Products by Revenue**  
   - Products with highest revenue (`total_price`).
   - Example:

| product_id | total_price |
|------------|-------------|
| 504        | 96.0        |
| 505        | 75.0        |
| 501        | 63.0        |
| 502        | 60.0        |
| 506        | 50.0        |

4. **Daily Revenue Trends**  
   - Revenue per order date.
   - Example:

| order_date | total_price |
|------------|------------|
| 2024-01-01 | 21.0       |
| 2024-01-02 | 20.0       |
| 2024-01-03 | 21.0       |
| 2024-01-04 | 60.0       |
| 2024-01-05 | 42.0       |
| 2024-01-06 | 40.0       |
| 2024-01-07 | 7.0        |
| 2024-01-08 | 36.0       |
| 2024-01-09 | 75.0       |
| 2024-01-10 | 50.0       |

