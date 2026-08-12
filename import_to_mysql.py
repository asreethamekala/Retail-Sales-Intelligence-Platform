import os
import pandas as pd
from sqlalchemy import create_engine

# ==========================================
# CSV File
# ==========================================

csv_path = r"C:\Users\asree\OneDrive\projects\Retail-Sales-Intelligence-Platform\Dataset\Cleaned_Data\cleaned_superstore_mysql.csv"

if not os.path.exists(csv_path):
    raise FileNotFoundError(
        f"CSV file not found: {csv_path}"
    )

# Read CSV
df = pd.read_csv(csv_path)

print(f"Rows in CSV: {len(df)}")

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

# ==========================================
# Create Database Connection
# ==========================================

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================================
# Import Data into MySQL
# ==========================================

df.to_sql(
    name="final_sample_superstore",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data imported successfully!")
