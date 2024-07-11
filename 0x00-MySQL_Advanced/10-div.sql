-- A function that divides two numbers
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS DECIMAL
BEGIN
  IF b = 0 THEN
    RETURN 0
  END IF;
  RETURN a / b;
END $$
DELIMITER ;
