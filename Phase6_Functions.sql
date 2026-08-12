USE sales_analysis;

-- Function to calculate Profit Margin
DELIMITER $$

CREATE FUNCTION GetProfitMargin(
    sales DECIMAL(10,2),
    profit DECIMAL(10,2)
)
RETURNS DECIMAL(10,2)
DETERMINISTIC

BEGIN
    IF sales = 0 THEN
        RETURN 0;
    END IF;

    RETURN (profit / sales) * 100;
END $$

DELIMITER ;

-- Test the function
SELECT
    Product_Name,
    Sales,
    Profit,
    GetProfitMargin(Sales, Profit) AS Profit_Margin
FROM Final_Sample_Superstore
LIMIT 10;