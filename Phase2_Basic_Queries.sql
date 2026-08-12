-- Use the database-- 
USE sales_analysis;   
-- using first 10 records-- 
SELECT *
FROM Final_Sample_Superstore
LIMIT 10;
-- Display only selected columns-- 
SELECT Customer_Name,
       Product_Name,
       Sales,
       Profit
FROM Final_Sample_Superstore
LIMIT 10;
-- Find all orders with Sales greater than 1000-- 
SELECT Customer_Name,
       Product_Name,
       Sales
FROM Final_Sample_Superstore
WHERE Sales > 1000;
-- Find all Technology products-- 
SELECT Product_Name,
       Category,
       Sales
FROM Final_Sample_Superstore
WHERE Category = 'Technology';
-- Display products sorted by highest sales-- 
SELECT Product_Name,
       Sales
FROM Final_Sample_Superstore
ORDER BY Sales DESC;
-- Display products sorted by lowest sales-- 
SELECT Product_Name,
       Sales
FROM Final_Sample_Superstore
ORDER BY Sales ASC;
-- Display all unique categories-- 
SELECT DISTINCT Category
FROM Final_Sample_Superstore;
-- SELECT COUNT(*) AS TotalOrders-- 
SELECT COUNT(*) AS TotalOrders
FROM Final_Sample_Superstore;