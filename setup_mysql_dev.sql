-- create database hbnb_dev_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create new user named hbnb_dev at localhosts
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on database performance_schema
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- grant select privilege to user hbnb_dev on performance_schema database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
