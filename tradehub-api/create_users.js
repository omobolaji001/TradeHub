const User = require('./models/user');
const sequelize = require('./config/db');


updates = {id: 100, fullName: "Ifafunto Ibrahim James", email: "ifajames@gmail.com"};
data = [];
for (const attr in updates) {
  data.push(attr);
}
console.log(data.length);

User.findByPk(2).then((user) => {
  for (const attr in updates) {
    if (updates.hasOwnProperty(attr) && attr !== 'id') {
      user[attr] = updates[attr];
    }
  }
  user.save();
  console.log(user.toJSON());
}).catch((err) => {
  console.error(err.errors[0].message);
});
