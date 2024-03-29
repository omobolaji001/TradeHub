require('dotenv').config();

const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', async (req, res) => {
  res.json({ msg: 'You should not be here' });
});

app.use('/api/v1/users', require('./routes/users.routes.js'));
app.use('/api/v1/businesses', require('./routes/businesses.routes.js'));
app.use('/api/v1/products', require('./routes/products.routes.js'));



const port = process.env.PORT || 8000;





app.listen(port, () => {
  console.log('listening at port ' + port);
});
