const sequelize = require('../config/db');
const User = require('./user');
const Business = require('./business');
const Product = require('./product');


User.belongsToMany(Business, {through: 'business_owner'});
Business.belongsToMany(User, {through: 'business_owner'});

Business.hasMany(Product);
Product.belongsTo(Business);

sequelize.sync({ alter: true });
