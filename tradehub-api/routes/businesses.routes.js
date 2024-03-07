const router = require('express').Router();
const {
  getBusiness,
  getBusinesses,
  createBusiness,
  updateBusiness,
  deleteBusiness
} = require('../controllers/businesses.controller.js');
const { 
  getProducts, 
  createProduct } = require('../controllers/products.controller.js');


router.get('/', getBusinesses);
router.get('/:businessId', getBusiness);
router.get('/:businessId/products', getProducts);
router.post('/:businessId/products', createProduct);
router.post('/', createBusiness);
router.put('/:businessId', updateBusiness);
router.delete('/:businessId', deleteBusiness);

module.exports = router;
