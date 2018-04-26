from flask import render_template
from flask.blueprints import Blueprint
from .models import *

module_one = Blueprint('module_one', __name__, template_folder='templates', static_folder='static')


@module_one.route("/")
@module_one.route("/index.html")
def index():
    return render_template('pages/index.html', title='Home')


@module_one.route("/entries")
def db_entries():
    user = Item.query.order_by(Item.name).all()
    return render_template('pages/index.html', title='Entries', user=user)
