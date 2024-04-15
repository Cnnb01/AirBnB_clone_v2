-- a script that prepares a MySQL server for the project
IF NOT EXISTS CREATE DATABASE hbnb_dev_db;
IF NOT EXISTS CREATE USER hbnb_dev IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db TO hbnb_dev;
GRANT SELECT ON performance_schema TO hbnb_dev;