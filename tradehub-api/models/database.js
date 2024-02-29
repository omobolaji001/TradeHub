const dbConfig = require('../config/db.js')
const Sequelize = require('sequelize')

const sequelize = new Sequelize(
  dbConfig.DB,
  dbConfig.USER,
  dbConfig.PASSWORD, 
  {host: dbConfig.HOST, dialect: 'mysql'}
  );


const User = require('./user.js')(sequelize, Sequelize)
const Business = require('./business.js')(sequelize, Sequelize)
const Product = require('./product.js')(sequelize, Sequelize)


// --------------------------------------Relationships----------------------------------------------
User.belongsToMany(Business, {through: 'business_owner'});
Business.belongsToMany(User, {through: 'business_owner'});
Business.hasMany(Product, {foreignKey: 'business_id'});

module.exports = {
    sequelize, 
    Sequelize, 
    User, Business, Product
};
