USE sales_analysis;
-- PROCEDURE 1
DELIMITER $$
CREATE PROCEDURE GetSalesByCategory(IN category_name VARCHAR(100))
 BEGIN
     SELECT *
     FROM Final_Sample_Superstore
     WHERE Category = category_name;
 END $$
 DELIMITER ;
CALL GetSalesByCategory('Technology');

-- PROCEDURE 2
  DELIMITER $$
 CREATE PROCEDURE GetTop10Products()
 BEGIN
     SELECT Product_Name,
            Sales
     FROM Final_Sample_Superstore
     ORDER BY Sales DESC
     LIMIT 10;
 END $$
 DELIMITER ;
CALL GetTop10Products();