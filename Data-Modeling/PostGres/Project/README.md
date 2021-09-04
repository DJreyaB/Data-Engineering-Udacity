# Data Modeling With Postgres

## Installation
The provided requirements file contains all external python libraries needed for to run this project. Install using:
```
pip install -r requirements.txt
```
##### Note : Does not include dependencies that should be automatically downloaded with libraries

## Purpose

Sparkify, a music streaming startup, would like to analyze their song and user activity data from their app. The raw data was stored within multiple JSON files. The file create_table.py will create the structure of the tables within the data base. 

## Execution
1. Run create_tables.py using "python create_tables.py" in terminal.
2. Run cells in test.ipynb to verify tables were created correctly.
3. Run etl.py using "python create_tables.py" in terminal.

## Schema Design

The database is designed using a star schema, a great design choice for queries with aggregation.  
The fact table is songplays and all other tables are dimension tables relating to their namesake. For example, the user table includes dimensions related to users. 

### related files
1. create_tables.py
    - Includes functions for database creation and drop/create table query exection.
    - Pulls queries from sql_queries.py

2. sql_queries.py
    - Contains queries for inserting, dropping, and creating tables

### Fact Table

songplays - records in log data associated with song plays i.e. records with page NextSong

songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables

users - users in the app  
user_id, first_name, last_name, gender, level

songs - songs in music database  
song_id, title, artist_id, year, duration

artists - artists in music database  
artist_id, name, location, latitude, longitude

time - timestamps of records in songplays broken down into specific units  
start_time, hour, day, week, month, year, weekday

## ETL Pipeline


Extract : The JSON data is pulled from its respective location and stored within a pandas DataFrame

Transform : The time data is give as milliseconds. To convert it to different time metrics the milliseconds has to be converted to datatime(timestamp) and then extract the metric. 

Load : The data is then inserted into postgres tables using python passed to the postgres queries.

### Related Files
1. etl.py
    - Includes functions for processing json files and inserting data into database.

#### Miscellaneous Files
1. etl.ipynb
    - Step by step testing of etl.py. 

2. test.ipynb
    - Run to test table creation and insertion was done correctly.
