import pandas as pd
from sqlalchemy import create_engine

# CSV file path
csv_path = r"C:\Users\asree\OneDrive\projects\Retail-Sales-Intelligence-Platform\Dataset\Cleaned_Data\cleaned_superstore_mysql.csv"

# Read CSV
df = pd.read_csv(csv_path)

print(f"Rows in CSV: {len(df)}")

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:3306@localhost:3306/sales_analysis"
)

# Import data into MySQL
df.to_sql(
    name="final_sample_superstore",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data imported successfully!")