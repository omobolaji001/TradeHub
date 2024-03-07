const sequelize = require('../config/db');
const Product = require('../models/product');
const Business = require('../models/business');


const getProducts = ((req, res) => {
  const businessId = Number(req.params.businessId);
  Product.findAll().then((data) => {
    all_products = [];
    data.forEach((product) => {
      all_products.push(product.toJSON());
    });
    const products = [];
    all_products.forEach((product) => {
      if (product.businessId === businessId) {
        products.push(product);
      }
    });
    res.status(200).json(products);
  }).catch((err) => {
    console.error(err);
    res.status(500).json({ error: 'Internal server error'});
  })
});



const getProduct = ((req, res) => {
  const productId = Number(req.params.productId);
  Product.findByPk(productId).then((product) => {
    if (!product) {
      return res.status(404).json({error: 'Not found'});
    }
    res.status(200).json(product);
  }).catch((err) => {
    console.error(err);
  });
});


const createProduct = ((req, res) => {
  
  const newProduct = {
    productName: req.body.productName,
    description: req.body.description,
    stockQuantity: req.body.stockQuantity,
    price: req.body.price,
    category: req.body.category,
    businessId: Number(req.params.businessId)
  };

  Product.create(newProduct).then((data) => {
    res.status(201).json(data);
  }).catch((err) => {
    console.log(err);
    return res.status(500).json({error: 'Internal server error'});
  });
});


const updateProduct = ((req, res) => {
  const productId = Number(req.params.productId);
  Product.findByPk(productId).then((product) => {
    if (!product) {
      return res.status(404).json({error: 'Not found'});
    }
    for (const attr in req.body) {
      if (req.body.hasOwnProperty(attr) && attr !== 'id') {
        product[attr] = req.body[attr];
      }
    }
    product.save();
    res.status(201).json(product);
  }).catch((err) => {
    res.status(500).json({error: 'Internal server error'});
  });
});


const deleteProduct = ((req, res) => {
  const productId = Number(req.params.productId);
  Product.findByPk(productId).then((product) => {
    if (!product) {
      return res.status(404).json({error: 'Not found'});
    }
    product.destroy();
    res.status(200).json({});
  }).catch((err) => {
    res.status(500).json({error: 'Internal server error'});
  });
});


module.exports = { 
	getProducts, 
	getProduct, 
	createProduct, 
	updateProduct, 
	deleteProduct 
};
