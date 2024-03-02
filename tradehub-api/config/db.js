const { Sequelize } = require('sequelize');

const dotenv = require('dotenv');
dotenv.config();

const sequelize = new Sequelize(
  process.env.MYSQL_DB,
  process.env.MYSQL_USER,
  process.env.MYSQL_PWD, {
  host: process.env.MYSQL_HOST,
  dialect: 'mysql'
});

module.exports = sequelize;
