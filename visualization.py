import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# ==========================================
# MySQL Configuration
# ==========================================

DB_USER = "root"
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "sales_analysis"

if not DB_PASSWORD:
    raise ValueError(
        "MYSQL_PASSWORD environment variable is not set."
    )

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================================
# 1. Sales by Category
# ==========================================

query = """
SELECT Category, SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8, 5))
plt.bar(df["Category"], df["Total_Sales"])

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()


# ==========================================
# 2. Sales Distribution by Category
# ==========================================

plt.figure(figsize=(8, 8))

plt.pie(
    df["Total_Sales"],
    labels=df["Category"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Category")
plt.axis("equal")
plt.show()


# ==========================================
# 3. Monthly Sales Trend
# ==========================================

query = """
SELECT
    DATE_FORMAT(Order_Date, '%%Y-%%m') AS Month,
    SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY DATE_FORMAT(Order_Date, '%%Y-%%m')
ORDER BY DATE_FORMAT(Order_Date, '%%Y-%%m');
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(12, 6))

plt.plot(
    df["Month"],
    df["Total_Sales"],
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()


# ==========================================
# 4. Sales vs Profit
# ==========================================

query = """
SELECT Sales, Profit
FROM final_sample_superstore;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Sales"],
    df["Profit"],
    alpha=0.5
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)

plt.tight_layout()
plt.show()


# ==========================================
# 5. Distribution of Sales
# ==========================================

query = """
SELECT Sales
FROM final_sample_superstore;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8, 5))

plt.hist(
    df["Sales"],
    bins=30
)

plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid(True)

plt.tight_layout()
plt.show()


# ==========================================
# 6. Profit Outliers
# ==========================================

query = """
SELECT Profit
FROM final_sample_superstore;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(6, 6))

plt.boxplot(df["Profit"])

plt.title("Profit Outliers")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()


# ==========================================
# 7. Top 10 Customers
# ==========================================

query = """
SELECT
    Customer_Name,
    SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(10, 6))

plt.barh(
    df["Customer_Name"],
    df["Total_Sales"]
)

plt.title("Top 10 Customers")
plt.xlabel("Total Sales")
plt.ylabel("Customer")

plt.tight_layout()
plt.show()


# ==========================================
# 8. Monthly Sales Area Chart
# ==========================================

query = """
SELECT
    DATE_FORMAT(Order_Date, '%%Y-%%m') AS Month,
    SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY DATE_FORMAT(Order_Date, '%%Y-%%m')
ORDER BY DATE_FORMAT(Order_Date, '%%Y-%%m');
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(12, 5))

plt.fill_between(
    df["Month"],
    df["Total_Sales"]
)

plt.xticks(rotation=45)

plt.title("Monthly Sales Area Chart")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

print("All visualizations completed successfully!")
