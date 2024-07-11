-- A query for bands that use the glam rock style
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan 
FROM metal_bands
WHERE style LIKE '%Glam rock%';
