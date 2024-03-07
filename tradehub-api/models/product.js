const { DataTypes } = require('sequelize');
<<<<<<< HEAD

module.exports = (sequelize, Sequelize) => {
    const Product = sequelize.define('product', {
        id: {
          type: DataTypes.INTEGER,
          autoIncrement: true,
          unique: true,
          primaryKey: true
        },
        product_name: {
          type: DataTypes.STRING,
          allowNull: false
        },
        description: {
          type: DataTypes.STRING,
        },
        stock_quantity: {
          type: DataTypes.INTEGER,
        },
        price: {
          type: DataTypes.INTEGER,
          allowNull: false
        },
        category: {
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
    
    return Product;
}
=======
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
>>>>>>> main
