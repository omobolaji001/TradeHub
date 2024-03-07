const { DataTypes } = require('sequelize');
const sequelize = require('../config/db');

const Product = sequelize.define('product', {
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    unique: true,
    primaryKey: true
  },
  productName: {
    type: DataTypes.STRING,
    allowNull: false
  },
  description: {
    type: DataTypes.STRING
  },
  stockQuantity: {
    type: DataTypes.INTEGER,
    defaultValue: 0
  },
  price: {
    type: DataTypes.INTEGER,
    allowNull: false,
    defaultValue: 0
  },
  category: {
    type: DataTypes.STRING
  },
  businessId: {
    type: DataTypes.INTEGER,
    allowNull: false
  }
});

module.exports = Product;
