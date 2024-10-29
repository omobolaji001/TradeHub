# TradeHub

**TradeHub** is an e-commerce platform where merchants can advertise their products, and customers can browse and purchase items. The platform is built using a Flask API for the backend, PostgreSQL for database management, and React for the frontend interface.

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

TradeHub is designed to facilitate seamless interaction between merchants and customers. Merchants can create an account to list and manage their products, while customers can browse, search, and purchase these products. The platform supports a variety of categories and aims to provide a user-friendly experience for both sellers and buyers.

## Tech Stack

- **Backend**: Flask (Python) API
- **Frontend**: React (JavaScript) 
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Styling**: CSS, Material-UI
- **Deployment**: Docker, Nginx (Optional for production)

## Features

### User (Customer)

- Browse and search products by categories.
- Add products to the shopping cart.
- Place orders and view order history.
- User authentication (login, registration).

### Merchant

- Register and create a merchant account.
- Add, update, and manage products.
- View orders from customers.
- Receive customer feedback.

### Admin

- Monitor users and merchants.
- Manage platform settings and analytics.

### General

- Secure user authentication using JWT.
- Responsive design for mobile and desktop.
- Database schema designed for scalable, multi-user e-commerce.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- Node.js (v14+)
- PostgreSQL
- Docker (Optional for production)

### Backend Setup (Flask API)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/tradehub.git
   cd tradehub
