-- a trigger to reset a boolean when email changes
DROP TRIGGER IF EXISTS after_email_change;
DELIMITER $$
CREATE TRIGGER after_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF OLD.email != NEW.email THEN
    SET NEW.valid_email = 0;
  END IF;
END $$
DELIMITER ;
