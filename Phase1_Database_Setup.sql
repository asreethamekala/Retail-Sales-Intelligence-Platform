USE sales_analysis;

CREATE TABLE Final_Sample_Superstore (
    Category VARCHAR(100),
    City VARCHAR(100),
    Country VARCHAR(100),
    Customer_ID VARCHAR(50),
    Customer_Name VARCHAR(255),
    Discount DECIMAL(10,2),
    Market VARCHAR(50),
    Record_Count INT,
    Order_Date DATE,
    Order_ID VARCHAR(50),
    Order_Priority VARCHAR(50),
    Product_ID VARCHAR(50),
    Product_Name VARCHAR(255),
    Profit DECIMAL(12,2),
    Quantity INT,
    Region VARCHAR(100),
    Row_ID INT,
    Sales DECIMAL(12,2),
    Segment VARCHAR(50),
    Ship_Date DATE,
    Ship_Mode VARCHAR(100),
    Shipping_Cost DECIMAL(12,2),
    State VARCHAR(100),
    Sub_Category VARCHAR(100),
    Year INT,
    Market2 VARCHAR(50),
    weeknum INT
);
SHOW VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 1;
SHOW VARIABLES LIKE 'local_infile';






USE sales_analysis;

LOAD DATA LOCAL INFILE 'C:/Users/asree/OneDrive/projects/Retail-Sales-Intelligence-Platform/Dataset/Cleaned_Data/Final_Sample_Superstore_UTF8.csv'
INTO TABLE Final_Sample_Superstore
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Category, City, Country, Customer_ID, Customer_Name, Discount, Market, Record_Count,
 Order_Date, Order_ID, Order_Priority, Product_ID, Product_Name, Profit, Quantity,
 Region, Row_ID, Sales, Segment, Ship_Date, Ship_Mode, Shipping_Cost,
 State, Sub_Category, Year, Market2, weeknum);
 
 SELECT COUNT(*) FROM Final_Sample_Superstore;
 
 SELECT COUNT(*) AS TotalRows
FROM Final_Sample_Superstore;

SELECT COUNT(*) AS TotalRows
FROM Final_Sample_Superstore;

SELECT * FROM Final_Sample_Superstore
LIMIT 10;