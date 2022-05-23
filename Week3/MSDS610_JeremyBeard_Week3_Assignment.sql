--Jeremy Beard, MSDS610, Week3 Assignment

CREATE DATABASE readychef;

--After creating the database, I then exited psql and loaded the sql file by performing "psql readychef < readychef.sql"

--I also entered "\c readychef" to switch to the dataset

--Get the average, min and max price for each meal type.
SELECT type, MIN(price), MAX(price), AVG(price), FROM meals GROUP BY type ORDER BY type;

--Using the WHERE clause, write a new SELECT statement that returns all rows where Campaign_ID is equal to FB .
SELECT userid, campaign_id from users WHERE campaign_id = 'FB';

--Write a query to get the count of just the users who came from Facebook.
SELECT campaign_id, COUNT(userid) FROM users WHERE campaign_id = 'FB' GROUP BY campaign_id;

--Now, count the number of users coming from each service. Here you'll have to group by the column you're selecting with a GROUP BY clause.
SELECT campaign_id, COUNT(userid) FROM users GROUP BY campaign_id;

--Write a query to get one table that joins the events table with the users table (on userid).
ALTER TABLE events RENAME COLUMN userid TO userid_events;
ALTER TABLE users RENAME COLUMN userid TO userid_users;
SELECT * FROM users INNER JOIN events ON userid_users = userid_events;