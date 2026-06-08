# 📦 Dataset Information

## Dataset Name
**Supermarket Sales Dataset**

## Download Link
[Kaggle — Supermarket Sales](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)

Direct CSV (alternative):
```
https://raw.githubusercontent.com/dsrscientist/dataset1/master/supermarket_sales.csv
```

## File Name Expected by the App
```
sales.csv
```
Place this file in the **same folder** as `app.py` before running.

---

## Columns Used by the Dashboard

| Column         | Type    | Description                              |
|----------------|---------|------------------------------------------|
| `Total`        | float   | Total purchase amount (incl. tax)        |
| `Quantity`     | int     | Number of items purchased                |
| `Rating`       | float   | Customer satisfaction rating (1–10)      |
| `Product line` | string  | Product category (e.g. Food, Fashion)    |

## Full Column List

| Column              | Description                          |
|---------------------|--------------------------------------|
| Invoice ID          | Unique transaction identifier        |
| Branch              | Store branch (A, B, C)               |
| City                | City of branch                       |
| Customer type       | Member or Normal                     |
| Gender              | Customer gender                      |
| Product line        | Product category                     |
| Unit price          | Price per item                       |
| Quantity            | Items purchased                      |
| Tax 5%              | 5% tax on subtotal                   |
| Total               | Total amount including tax           |
| Date                | Date of purchase                     |
| Time                | Time of purchase                     |
| Payment             | Payment method                       |
| cogs                | Cost of goods sold                   |
| gross margin %      | Gross margin percentage              |
| gross income        | Gross income                         |
| Rating              | Customer rating (1–10)               |

## Size
- **Rows:** 1,000
- **Columns:** 17
- **No missing values**
