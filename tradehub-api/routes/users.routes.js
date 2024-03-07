const router = require('express').Router();
const {
  getUser,
  getUsers,
  createUser,
  updateUser,
  deleteUser
} = require('../controllers/users.controller.js');

router.get('/', getUsers);
router.get('/:userId', getUser);
router.post('/', createUser);
router.put('/:userId', updateUser);
router.delete('/:userId', deleteUser);

module.exports = router;
