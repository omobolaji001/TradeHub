const router = require('express').Router();
const { getBusiness, 
	getBusinesses, 
	createBusiness,
        updateBusiness,
	deleteBusiness } = require('../controllers/businesses.controller.js')

router.get('/', getBusinesses);
router.get('/:businessId', getBusiness);
router.post('/', createBusiness);
router.put('/:businessId', updateBusiness);
router.delete('/:businessId', deleteBusiness);

module.exports = router
