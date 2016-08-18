# -*- coding: utf-8 -*-
from flask import Blueprint
hr=Blueprint('hr',__name__)

from . import views,forms,models