import pymysql
import pandas as pd

# Connect to MySQL
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="3306",
    database="sales_analysis",
    port=3306
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