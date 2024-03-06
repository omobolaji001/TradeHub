const router = require('express').Router();
const { getProduct, 
	getProducts, 
	createUser,
        updateUser,
	deleteUser } = require('../controllers/products.controller.js')

router.get('/', getProducts);
router.get('/:productId', getProduct);
router.post('/', createUser);
router.put('/:userId', updateUser);
router.delete('/:userId', deleteUser);

module.exports = router
