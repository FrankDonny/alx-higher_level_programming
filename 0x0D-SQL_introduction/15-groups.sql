-- script to list all records with the same score

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
