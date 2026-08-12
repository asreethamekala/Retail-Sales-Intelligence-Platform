-- Total Sales by Category-- 
SELECT Category,
       SUM(Sales) AS Total_Sales
FROM Final_Sample_Superstore
GROUP BY Category;
-- Total Profit by Category-- 
SELECT Category,
       SUM(Profit) AS Total_Profit
FROM Final_Sample_Superstore
GROUP BY Category;
-- Average Sales by Category-- 
SELECT Category,
       AVG(Sales) AS Average_Sales
FROM Final_Sample_Superstore
GROUP BY Category;
-- Number of Orders in Each Category-- 
SELECT Category,
       COUNT(*) AS Total_Orders
FROM Final_Sample_Superstore
GROUP BY Category;
-- Top 10 Highest Selling Products--
 SELECT Product_Name,
       Sales
FROM Final_Sample_Superstore
ORDER BY Sales DESC
LIMIT 10;
-- Top 10 Most Profitable Products--
 SELECT Product_Name,
       Profit
FROM Final_Sample_Superstore
ORDER BY Profit DESC
LIMIT 10;
-- Sales by Region--
 SELECT Region,
       SUM(Sales) AS Total_Sales
FROM Final_Sample_Superstore
GROUP BY Region;
-- Profit by Region--
 SELECT Region,
       SUM(Profit) AS Total_Profit
FROM Final_Sample_Superstore
GROUP BY Region;
-- Customers Who Purchased the Most Items--
 SELECT Customer_Name,
       SUM(Quantity) AS Total_Quantity
FROM Final_Sample_Superstore
GROUP BY Customer_Name
ORDER BY Total_Quantity DESC
LIMIT 10;
-- Categories Having Sales Greater Than 1,000,000--
 SELECT Category,
       SUM(Sales) AS Total_Sales
FROM Final_Sample_Superstore
GROUP BY Category
HAVING SUM(Sales) > 1000000;