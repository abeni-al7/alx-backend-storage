-- A stored procedure that computes all weighted averages
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update all users' average scores in one go
    UPDATE users u
    JOIN (
        SELECT 
            c.user_id,
            SUM(c.score * p.weight) / SUM(p.weight) AS avg_weighted_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        GROUP BY c.user_id
    ) weighted_scores ON u.id = weighted_scores.user_id
    SET u.average_score = weighted_scores.avg_weighted_score;
    
    -- For users without any corrections, set average_score to 0
    UPDATE users u
    LEFT JOIN corrections c ON u.id = c.user_id
    SET u.average_score = 0
    WHERE c.user_id IS NULL;
END $$

DELIMITER ;
