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
    type: DataTypes.STRING,
  },
  stockQuantity: {
    type: DataTypes.INTEGER,
  },
  price: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  category: {
    type: DataTypes.STRING
  }
});

module.exports = Product;
>>>>>>> main
