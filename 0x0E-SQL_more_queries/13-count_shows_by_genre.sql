-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- lists all rows of database meeting a condition
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
