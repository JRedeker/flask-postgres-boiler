from flask import render_template
from flask.blueprints import Blueprint
from .models import *

module_two = Blueprint('views', __name__, template_folder='templates', static_folder='static')


@module_two.route("/two")
@module_two.route("/index_two.html")
def index():
    return render_template('pages/index.html', title='Home')


@module_two.route("/entries_two")
def db_entries():
    entries = Table.query.order_by(Table.name).all()
    return render_template('pages/entries.html', title='Entries', entries=entries)
