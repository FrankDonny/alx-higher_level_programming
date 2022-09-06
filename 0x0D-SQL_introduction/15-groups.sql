-- script to list all records with the same score

SELECT COUNT(score) as score, 'number'
FROM second_table
GROUP BY score;
