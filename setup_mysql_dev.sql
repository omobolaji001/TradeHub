-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS tradehub_db;
CREATE USER IF NOT EXISTS 'tradehub_dev'@'localhost' IDENTIFIED BY 'tradehub_pwd';
GRANT ALL PRIVILEGES ON `tradehub_db`.* TO 'tradehub_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tradehub_dev'@'localhost';
FLUSH PRIVILEGES;
