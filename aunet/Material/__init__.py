# -*- coding: utf-8 -*-
from flask import Blueprint

material = Blueprint('material', __name__, url_prefix='/Material',
                     static_folder='../static/Material', template_folder='../templates/Material')

from . import views
