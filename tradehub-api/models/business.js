const { DataTypes } = require('sequelize');

module.exports = (sequelize, Sequelize) => {
    const Business = sequelize.define('business', {
        id: {
          type: DataTypes.INTEGER,
          autoIncrement: true,
          unique: true,
          primaryKey: true
        },
        business_name: {
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
        phone_number: {
          type: DataTypes.STRING
        },
        physical_address: {
          type: DataTypes.STRING
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

    return Business;
}