const { DataTypes } = require('sequelize');
const sequelize = require('../config/db');


const Business = sequelize.define('business', {
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    unique: true,
    primaryKey: true
  },
  businessName: {
    type: DataTypes.STRING,
    allowNull: false
  },
  description: {
    type: DataTypes.STRING,
    allowNull: false
  },
  email: {
    type: DataTypes.STRING,
    allowNull: false
  },
  phoneNumber: {
    type: DataTypes.STRING
  },
  physicalAddress: {
    type: DataTypes.STRING
  }
});

module.exports = Business;

