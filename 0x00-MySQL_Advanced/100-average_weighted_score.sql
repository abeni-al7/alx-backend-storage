-- A stored procedure that computes the weighted average of a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
  DECLARE total_weight INT;
  DECLARE weighted_sum FLOAT;

  SELECT SUM(p.weight) INTO total_weight
  FROM projects p
  JOIN corrections c ON p.id = c.project_id
  WHERE c.user_id = user_id;

  SELECT SUM(c.score * p.weight) INTO weighted_sum
  FROM corrections c
  JOIN projects p ON c.project_id = p.id
  WHERE c.user_id = user_id;

  UPDATE users
  SET average_score = weighted_sum / total_weight
  WHERE users.id = user_id;
END $$
DELIMITER ;
