# -*- coding: utf-8 -*-
from flask import Blueprint
grade=Blueprint('grade',__name__)

from . import views,forms,models