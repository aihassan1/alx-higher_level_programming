-- lists all cities contained in the database hbtn_0d_usa.

-- Each record should display: cities.id - cities.name - states.name

SELECT cities.id AS city_id , cities.name AS city_name, states.name AS state_name
FROM cities 
LEFT JOIN states
ON cities.state_id = states.id;