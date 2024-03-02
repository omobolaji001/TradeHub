const User = require('../models/user');
exports.home = async (req, res) => {
    res.status(400).json({
        msg: 'You have successfully reached TradeHub Users home page'
    })
}

const getUsers = ((req, res) => {
  User.findAll().then((data) => {
    users = [];
    data.forEach((user) => {
      users.push(user.toJSON());
    })
    res.status(200).json(users);
  }).catch((err) => {
    console.error(err);
    res.status(500).json({ error: 'Internal server error'});
  })
});


const getUser = ((req, res) => {
  const userId = Number(req.params.userId);
  User.findOne({where: {id: userId}}).then((user) => {
    if (!user) {
      return res.status(404).json({error: 'Not found'});
    }
    res.status(200).json(user);
  }).catch((err) => {
    console.error(err);
  });
});


module.exports = { getUsers, getUser };
