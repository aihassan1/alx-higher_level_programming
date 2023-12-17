-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2
-- cat 0-privileges.sql | mysql -hlocalhost -uroot -p
SHOW GRANT FOR 'user_0d_1 ' AND 'user_0d_2 ';