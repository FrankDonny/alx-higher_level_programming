-- script to list all cities of california that can be found in the database

SELECT * FROM states
WHERE name = 'California'
ORDER BY name;