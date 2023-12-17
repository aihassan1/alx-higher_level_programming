-- script that creates the MySQL server user user_0d_1.
-- user_0d_1 should have all privileges on your MySQL server
-- If the user user_0d_1 already exists,CODE WON'T FAIL

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* FOR 'user_0d_1'@'localhost';