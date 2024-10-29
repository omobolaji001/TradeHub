-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS tradehub_dev_db;
CREATE USER IF NOT EXISTS 'tradehub_dev'@'localhost' IDENTIFIED BY 'tradehub_dev_pwd';
GRANT ALL PRIVILEGES ON `tradehub_dev_db`.* TO 'tradehub_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tradehub_dev'@'localhost';
FLUSH PRIVILEGES;
