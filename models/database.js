const { Sequelize } = require('sequelize');
const User = require('./user');
const Business = require('./business');
const Product = require('./product');

const dotenv = require('dotenv');
dotenv.config();

const sequelize = new Sequelize(
  process.env.MYSQL_DB,
  process.env.MYSQL_USER,
  process.env.MYSQL_PWD, {
  host: process.env.MYSQL_HOST,
  dialect: 'mysql'
});

User.sync();
Business.sync();
Product.sync();

module.exports = sequelize;
