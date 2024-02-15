-- creates the database hbtn_0d_2 and the user user_0d_2 creates a database
-- creates a user grants SELECT privileges to a user
CREATE database IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
   ON `hbtn_0d_2`.*
   TO 'user_0d_2'@'localhost'
   IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
