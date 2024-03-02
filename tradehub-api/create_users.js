const User = require('./models/user');



const getUser = (userId) => {
  User.findOne({where: {id: userId}}).then((user) => {
    if (!user) {
      console.log("Not found");
      return
    }
    console.log(user.toJSON());
  }).catch((err) => {
    console.error(err);
  });
}

getUser(10);
