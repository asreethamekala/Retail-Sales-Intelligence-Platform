USE sales_analysis;
-- Create a log table 
 CREATE TABLE Sales_Log (
     Log_ID INT AUTO_INCREMENT PRIMARY KEY,
     Product_Name VARCHAR(255),
     Sales_Value DECIMAL(10,2),
     Log_Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 );
-- Create a trigger
 DELIMITER $$
 CREATE TRIGGER AfterSalesInsert
 AFTER INSERT ON Final_Sample_Superstore
 FOR EACH ROW
 BEGIN
     INSERT INTO Sales_Log(Product_Name, Sales_Value)
     VALUES (NEW.Product_Name, NEW.Sales);
 END $$
 DELIMITER ;
 -- Test the trigger 
 INSERT INTO Final_Sample_Superstore
 (Category, Product_Name, Sales)
 VALUES
 ('Technology','Test Product',5000);
-- Check whether the trigger worked 
 SELECT * FROM Sales_Log; 



