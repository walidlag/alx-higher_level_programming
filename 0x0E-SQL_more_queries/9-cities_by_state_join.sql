-- lists all cities contained in database hbtn_0d_usa
-- lists all rows of particular column in database
SELECT cities.id, cities.name, states.name
FROM cities
       INNER JOIN states
       ON states.id = cities.state_id
       ORDER BY cities.id;
