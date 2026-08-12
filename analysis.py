import os
import pymysql
import pandas as pd

# MySQL configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PORT = 3306
DB_NAME = "sales_analysis"

# Get password from environment variable
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")

if not DB_PASSWORD:
    raise ValueError(
        "MYSQL_PASSWORD environment variable is not set."
    )

# Connect to MySQL
connection = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    port=DB_PORT
)

# Load data
query = "SELECT * FROM final_sample_superstore"

df = pd.read_sql(query, connection)

print("=" * 60)
print("RETAIL SALES DATASET SUMMARY")
print("=" * 60)

print("\nTotal Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

connection.close()

print("\nAnalysis completed successfully!")
