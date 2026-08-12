import os
import pymysql

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

try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

    print("Connected to MySQL successfully!")

    cursor = connection.cursor()

    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    print("\nTables in the database:")

    for table in tables:
        print(table[0])

    cursor.close()
    connection.close()

except pymysql.MySQLError as e:
    print("MySQL connection error:", e)
