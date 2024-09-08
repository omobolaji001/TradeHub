#!/usr/bin/env python3
""" Blueprint for Authentication """
from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')
