const sequelize = require('../config/db');
const User = require('../models/user');
exports.home = async (req, res) => {
  res.status(400).json({
    msg: 'You have successfully reached TradeHub Users home page'
  });
};

const getUsers = (req, res) => {
  User.findAll().then((data) => {
    const users = [];
    data.forEach((user) => {
      users.push(user.toJSON());
    });
    res.status(200).json(users);
  }).catch((err) => {
    console.error(err);
    res.status(500).json({ error: 'Internal server error' });
  });
};

const getUser = (req, res) => {
  const userId = Number(req.params.userId);
  User.findOne({ where: { id: userId } }).then((user) => {
    if (!user) {
      return res.status(404).json({ error: 'Not found' });
    }
    res.status(200).json(user);
  }).catch((err) => {
    console.error(err);
  });
};

const createUser = (req, res) => {
  const newUser = {
    fullName: req.body.fullName,
    username: req.body.username,
    email: req.body.email,
    password: req.body.password
  };

  User.create(newUser).then((data) => {
    res.status(201).json(data);
  }).catch((err) => {
    console.log(err);
    return res.status(500).json({ error: 'Internal server error' });
  });
};

const updateUser = (req, res) => {
  const userId = Number(req.params.userId);
  User.findByPk(userId).then((user) => {
    if (!user) {
      return res.status(404).json({ error: 'Not found' });
    }
    for (const attr in req.body) {
      if (req.body.hasOwnProperty(attr) && attr !== 'id') {
        user[attr] = req.body[attr];
      }
    }
    user.save();
    res.status(201).json(user);
  }).catch((err) => {
    res.status(500).json({ error: 'Internal server error' });
  });
};

const deleteUser = (req, res) => {
  const userId = Number(req.params.userId);
  User.findByPk(userId).then((user) => {
    if (!user) {
      return res.status(404).json({ error: 'Not found' });
    }
    user.destroy();
    res.status(200).json({});
  }).catch((err) => {
    res.status(500).json({ error: 'Internal server error' });
  });
};

module.exports = {
  		   getUsers,
		   getUser,
		   createUser,
		   updateUser,
		   deleteUser
};
