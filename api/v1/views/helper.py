#!/usr/bin/env python3
""" Helper function """
from models.product import Product
from sqlalchemy.orm.exc import NoResultFound


def get_product_price(product_id):
    """ Retrieves the price of a product """
    try:
        product = Product.query.filter_by(id=product_id).first()
        return product.price
    except NoResultFound:
        return None
