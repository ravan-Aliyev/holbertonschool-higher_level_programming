-- Number by score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY number ORDER BY score DESC;