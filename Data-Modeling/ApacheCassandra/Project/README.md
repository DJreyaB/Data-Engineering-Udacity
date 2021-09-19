# Data Modeling with Apache Cassandra


## Installation
The provided requirements file contains all external python libraries needed to run this project. Install using:

```
pip install -r requirements.txt
```

##### Note : Does not include dependencies that should be automatically downloaded with libraries

## Purpose
Sparkify needs to analyze user activity data for their new music streaming app. The current database designs do not allow for easy query. The Cassandara tables are created to ease the analysis process.

## Queries

## 1
### Description  
Tasked with retrieving the artist, song title and song length heard during session id 338 and item in session 4. This table was partitioned by session id with clusters key of item in session. This seperates sessions into more granular parts based on their item in session.

## 2
### Description  
Tasked with retrieving the artist name, song (sorted by item in session), and first name and last name of user for the user with id 10 during session 182. This table was partitioned by both user id and session id and with clusters ordered by item in session, first name, and last name. Primary key are organized as such to make sure none of the details are combined or replaced with non-relevant values.

## 3
### Description  
Tasked with retrieving the first name and last name of every user who has listened to song "All Hands Against His Own". Table is partitioned by title with clusters ordered by user id to insure those all users who have heard the song are identified with their own row, including any users with same names.
