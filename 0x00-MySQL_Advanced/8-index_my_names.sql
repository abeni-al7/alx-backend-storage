-- An index for optimizing search by name
-- it optimizes search results
CREATE INDEX idx_name_first ON names(name(1));
