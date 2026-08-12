import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="3306",
        database="sales_analysis",
        port=3306
    )

    print("Connected to MySQL successfully!\n")

    cursor = connection.cursor()

    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(table[0])

    cursor.close()
    connection.close()

except Exception as e:
    print("Connection failed!")
    print(e)