USE sales_analysis;
-- Creating a Sales Summary View --
 CREATE VIEW Sales_Summary AS
SELECT
     Category,
     SUM(Sales) AS Total_Sales,
     SUM(Profit) AS Total_Profit,
     AVG(Sales) AS Average_Sales
 FROM Final_Sample_Superstore
 GROUP BY Category;
-- Display the View--
SELECT *
 FROM Sales_Summary;
-- Create a Top Customers View--
CREATE VIEW Top_Customers AS
 SELECT
     Customer_Name,
    SUM(Sales) AS Total_Sales
 FROM Final_Sample_Superstore
 GROUP BY Customer_Name;
-- Display the Top Customers View--
 SELECT *
FROM Top_Customers
ORDER BY Total_Sales DESC
LIMIT 10;


  