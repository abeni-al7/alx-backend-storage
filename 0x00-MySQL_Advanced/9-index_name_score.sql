-- An index for name and score in names
CREATE INDEX idx_name_first_score ON names(name(1), score);
