# -*- coding: utf-8 -*-
from flask import Blueprint
from itsdangerous import URLSafeTimedSerializer
from aunet import app

admin=Blueprint('admin',__name__,)
ts=URLSafeTimedSerializer(app.config['SECRET_KEY'])

from . import views