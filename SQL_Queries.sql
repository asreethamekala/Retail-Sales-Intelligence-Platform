USE sales_analysis;

SELECT COUNT(*) AS Total_Rows
FROM final_sample_superstore;

SELECT *
FROM final_sample_superstore
LIMIT 10;

SELECT Order_Date
FROM final_sample_superstore
LIMIT 10;

SELECT COUNT(*)
FROM final_sample_superstore
WHERE Order_Date IS NULL;

SELECT Sales
FROM final_sample_superstore
LIMIT 10;

USE sales_analysis;

SHOW TABLES;

SELECT * FROM top_customers;

SELECT COUNT(*) AS Total_Rows
FROM final_sample_superstore;

DESCRIBE final_sample_superstore;

USE sales_analysis;

SELECT COUNT(*) AS Total_Rows
FROM final_sample_superstore;

SELECT *
FROM final_sample_superstore
LIMIT 10;

SELECT SUM(Sales)
FROM final_sample_superstore;

SELECT AVG(Profit)
FROM final_sample_superstore;

SELECT Category,
       SUM(Sales) AS Total_Sales
FROM final_sample_superstore
GROUP BY Category;

SELECT
    COUNT(*) AS Row_Count,
    MIN(Order_Date) AS First_Date,
    MAX(Order_Date) AS Last_Date
FROM final_sample_superstore;

SELECT MIN(Order_Date), MAX(Order_Date)
FROM final_sample_superstore;

SELECT COUNT(*)
FROM final_sample_superstore
WHERE Order_Date IS NULL;

SELECT SUM(Sales) AS Total_Sales,
       SUM(Profit) AS Total_Profit
FROM final_sample_superstore;

SELECT COUNT(DISTINCT Customer_ID) AS Unique_Customers
FROM final_sample_superstore;
