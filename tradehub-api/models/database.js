const sequelize = require('../config/db.js')


try {
        sequelize.authenticate().then(() => {
           console.log('Connection has been established successfully.');
        }).catch((error) => {
           console.error('Unable to connect to the database: ', error.message);
        });
      
      const User = require('./user.js');
      const Business = require('./business.js');
      const Product = require('./product.js');
      
      
      // --------------------------------------Relationships----------------------------------------------
      User.belongsToMany(Business, {through: 'business_owner'});
      Business.belongsToMany(User, {through: 'business_owner'});
      Business.hasMany(Product, {foreignKey: 'businessId'});
      Product.belongsTo(Business);
      

      sequelize.sync({ alter: true });
} catch (error) {
    console.log(error.message)
};
