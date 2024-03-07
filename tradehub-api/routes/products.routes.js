const router = require('express').Router();
const {
  getProduct,
  getProducts,
  createProduct,
  updateProduct,
  deleteProduct
} = require('../controllers/products.controller.js');


router.get('/:productId', getProduct);
router.put('/:productId', updateProduct);
router.delete('/:productId', deleteProduct);

module.exports = router;
