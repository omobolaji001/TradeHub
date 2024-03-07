const sequelize = require('../config/db');
const Business = require('../models/business');

const getBusinesses = (req, res) => {
  Business.findAll().then((data) => {
    const businesses = [];
    data.forEach((business) => {
      businesses.push(business.toJSON());
    });
    res.status(200).json(businesses);
  }).catch((err) => {
    console.error(err);
    res.status(500).json({ error: 'Internal server error' });
  });
};

const getBusiness = (req, res) => {
  const businessId = Number(req.params.businessId);
  Business.findByPk(businessId).then((business) => {
    if (!business) {
      return res.status(404).json({ error: 'Not found' });
    }
    res.status(200).json(business);
  }).catch((err) => {
    console.error(err);
  });
};

const createBusiness = (req, res) => {
  const newBusiness = {
    businessName: req.body.businessName,
    description: req.body.description,
    email: req.body.email,
    phoneNumber: req.body.phoneNumber,
    physicalAddress: req.body.address
  };

  Business.create(newBusiness).then((data) => {
    res.status(201).json(data);
  }).catch((err) => {
    console.log(err);
    return res.status(500).json({ error: 'Internal server error' });
  });
};

const updateBusiness = (req, res) => {
  const businessId = Number(req.params.businessId);
  Business.findByPk(businessId).then((business) => {
    if (!business) {
      return res.status(404).json({ error: 'Not found' });
    }
    for (const attr in req.body) {
      if (req.body.hasOwnProperty(attr) && attr !== 'id') {
        business[attr] = req.body[attr];
      }
    }
    business.save();
    res.status(201).json(business);
  }).catch((err) => {
    res.status(500).json({ error: 'Internal server error' });
  });
};

const deleteBusiness = (req, res) => {
  const businessId = Number(req.params.businessId);
  Business.findByPk(businessId).then((business) => {
    if (!business) {
      return res.status(404).json({ error: 'Not found' });
    }
    business.destroy();
    res.status(200).json({});
  }).catch((err) => {
    res.status(500).json({ error: 'Internal server error' });
  });
};

module.exports = {
  		   getBusinesses,
		   getBusiness,
		   createBusiness,
		   updateBusiness,
		   deleteBusiness};
