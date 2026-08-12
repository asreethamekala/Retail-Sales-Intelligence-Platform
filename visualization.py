import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3306@localhost/sales_analysis")

query = """
SELECT Category, SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY Category;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8,5))
plt.bar(df["Category"], df["Total_Sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3306@localhost/sales_analysis")

query = """
SELECT Category, SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY Category;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8,8))

plt.pie(
    df["Total_Sales"],
    labels=df["Category"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Category")
plt.axis("equal")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# -------------------------------
# MySQL Connection
# -------------------------------
username = "root"
password = "3306"          # Your MySQL password
host = "localhost"
database = "sales_analysis"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:3306/{database}"
)

# -------------------------------
# Read Monthly Sales Data
# -------------------------------
query = """
SELECT
    DATE_FORMAT(Order_Date,'%%Y-%%m') AS Month,
    SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY DATE_FORMAT(Order_Date,'%%Y-%%m')
ORDER BY DATE_FORMAT(Order_Date,'%%Y-%%m');
"""

df = pd.read_sql(query, engine)

# -------------------------------
# Plot Line Chart
# -------------------------------
plt.figure(figsize=(12,6))

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

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3306@localhost/sales_analysis")

query = """
SELECT Sales, Profit
FROM final_sample_superstore;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8,6))
plt.scatter(df["Sales"], df["Profit"], alpha=0.5)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3306@localhost/sales_analysis")

query = """
SELECT Sales
FROM final_sample_superstore;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=30)

plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3306@localhost/sales_analysis")

query = """
SELECT Profit
FROM final_sample_superstore;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(6,6))
plt.boxplot(df["Profit"])

plt.title("Profit Outliers")
plt.ylabel("Profit")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3306@localhost/sales_analysis")

query = """
SELECT Customer_Name,
SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(10,6))
plt.barh(df["Customer_Name"], df["Total_Sales"])

plt.title("Top 10 Customers")
plt.xlabel("Total Sales")
plt.ylabel("Customer")

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3306@localhost/sales_analysis")

query = """
SELECT DATE_FORMAT(Order_Date,'%%Y-%%m') AS Month,
SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY Month
ORDER BY Month;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(12,5))
plt.fill_between(df["Month"], df["Total_Sales"])

plt.xticks(rotation=45)

plt.title("Monthly Sales Area Chart")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()