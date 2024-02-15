-- Displays the 3 cities with the highest average temperatures between July and August
CREATE TABLE IF NOT EXISTS temp_july_aug
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
