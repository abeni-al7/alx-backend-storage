DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE uid INT;
  DECLARE cur CURSOR FOR SELECT id FROM users;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO uid;
    IF done THEN
      LEAVE read_loop;
    END IF;

    DECLARE total_weight INT;
    DECLARE weighted_sum FLOAT;

    -- Calculate the total weight for the user
    SELECT SUM(p.weight) INTO total_weight
    FROM projects p
    JOIN corrections c ON p.id = c.project_id
    WHERE c.user_id = uid;

    -- Calculate the weighted sum for the user
    SELECT SUM(c.score * p.weight) INTO weighted_sum
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = uid;

    -- Update the user's average score
    IF total_weight > 0 THEN
      UPDATE users
      SET average_score = weighted_sum / total_weight
      WHERE id = uid;
    ELSE
      UPDATE users
      SET average_score = 0
      WHERE id = uid;
    END IF;
  END LOOP;

  CLOSE cur;
END $$

DELIMITER ;
