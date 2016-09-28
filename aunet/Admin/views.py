from . import admin
from flask import render_template

@admin.route('/index')
@admin.route('/')
def index():
	return render_template("Admin/index.html")
