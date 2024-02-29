const { DataTypes } = require('sequelize');
// const sequelize = require('./database');
// const Business = require('./business');


module.exports = (sequelize, Sequelize) => {
    const User = sequelize.define('user', {
        id: {
          type: DataTypes.INTEGER,
          autoIncrement: true,
          primaryKey: true
        },
        full_name: {
          type: DataTypes.STRING,
          allowNull: false
        },
        username: {
          type: DataTypes.STRING,
          allowNull: false
        },
        password: {
          type: DataTypes.STRING,
          allowNull: false
        },
        email: {
          type: DataTypes.STRING,
          allowNull: false
        },
        created_at: {
          type: DataTypes.DATE,
          defaultValue: DataTypes.NOW
        },
        updated_at: {
          type: DataTypes.DATE,
          defaultValue: DataTypes.NOW
        }
      }, {
        timestamps: false
      });

    return User;
}




