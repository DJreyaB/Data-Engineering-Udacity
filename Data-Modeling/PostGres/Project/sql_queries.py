# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users ;"
song_table_drop = "DROP TABLE IF EXISTS songs ;"
artist_table_drop = "DROP TABLE IF EXISTS artist ;"
time_table_drop = "DROP TABLE IF EXISTS time ;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
(
songplay_id SERIAL PRIMARY KEY,
start_time timestamp REFERENCES time,
user_id INT REFERENCES users,
level TEXT,
song_id TEXT REFERENCES songs,
artist_id TEXT REFERENCES artists,
session_id INT,
location TEXT,
user_agent TEXT
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users
(
user_id INT PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
gender TEXT,
level TEXT
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(
song_id TEXT PRIMARY KEY, 
title TEXT , 
artist_id TEXT REFERENCES artists, 
year INT, 
duration float)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
(artist_id TEXT PRIMARY KEY,
name TEXT,
location TEXT,
latitude float,
longitude float)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(start_time timestamp PRIMARY KEY,
hour INT,
day INT,
week INT,
month INT,
year INT,
weekday TEXT)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT 
    song_id,
    artist_id
FROM songs
WHERE title = %s
AND artist_id = %s
AND duration = %s
""")

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, artist_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]