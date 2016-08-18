# -*- coding: utf-8 -*-
from flask import Blueprint
material=Blueprint('material',__name__)

from . import views,forms,models