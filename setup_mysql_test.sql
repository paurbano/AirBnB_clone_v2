-- prepares a MySQL server for the project AirBnB Clone
-- Create a Db hbnb_test_db, user and assign privileges for test porpouses
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
FLUSH PRIVILEGES;
