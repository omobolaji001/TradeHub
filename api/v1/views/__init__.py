#!/usr/bin/env python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
auth = Blueprint('auth', __name__, url_prefix='/auth')


from api.v1.views.users import *
from api.v1.views.orders import *
from api.v1.views.carts import *
from api.v1.views.products import *
from api.v1.views.categories import *
from api.v1.views.index import *
