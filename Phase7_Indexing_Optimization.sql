USE sales_analysis;
-- Create an index on Category--
 CREATE INDEX idx_category
ON Final_Sample_Superstore(Category);
-- Create an index on Customer_Name--
CREATE INDEX idx_customer
ON Final_Sample_Superstore(Customer_Name);
-- Create an index on Order_Date
CREATE INDEX idx_orderdate
ON Final_Sample_Superstore(Order_Date);
-- Verify indexes
SHOW INDEX
FROM Final_Sample_Superstore;
-- Use EXPLAIN 
SELECT *
FROM Final_Sample_Superstore
WHERE Category='Technology';
-- EXPLAIN
SELECT *
FROM Final_Sample_Superstore
WHERE Customer_Name='Tamara Chand';
-- Query using the indexes 
SELECT *
FROM Final_Sample_Superstore
 WHERE Category='Technology'
LIMIT 10;
SELECT Customer_Name,
       SUM(Sales) AS TotalSales
FROM Final_Sample_Superstore
GROUP BY Customer_Name
ORDER BY TotalSales DESC
LIMIT 10;