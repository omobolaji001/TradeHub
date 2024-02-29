-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS tradehub_test_db;
CREATE USER IF NOT EXISTS 'tradehub_test'@'localhost' IDENTIFIED BY 'tradehub_test_pwd';
GRANT ALL PRIVILEGES ON `tradehub_test_db`.* TO 'tradehub_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'tradehub_test'@'localhost';
FLUSH PRIVILEGES;
