-- Number of genres
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_show_genres.genre_id IS NOT NULL GROUP BY tv_genres.name ORDER BY COUNT(*) DESC;