const router = require('express').Router();
const { getUser, getUsers } = require('../controllers/users.controller.js')

router.get('/', getUsers);
router.get('/:userId', getUser);

module.exports = router
