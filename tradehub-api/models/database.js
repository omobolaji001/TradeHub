const dbConfig = require('../config/db.js')
const Sequelize = require('sequelize')

try {
    const sequelize = new Sequelize(
        dbConfig.DB,
        dbConfig.USER,
        dbConfig.PASSWORD, 
        {host: dbConfig.HOST, dialect: 'postgres'}
        );

        sequelize.authenticate().then(() => {
           console.log('Connection has been established successfully.');
        }).catch((error) => {
           console.error('Unable to connect to the database: ', error.message);
        });
      
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
} catch (error) {
    console.log(error.message)
}

