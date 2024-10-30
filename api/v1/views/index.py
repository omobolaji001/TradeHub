#!/usr/bin/python3
""" Index """
from models.user import User
from models.business import Business
from models.product import Product
from models.category import Category
from models.order import Order
from models.cart import Cart
from models.shipment import Shipment
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [User, Business, Product, Category, Order, Cart, Shipment]
    names = ["businesses", "categories", "shipments"
             "carts", "orders", "users", "products"]

    num_objs = {}
    for i in range(len(classes)):
       num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
