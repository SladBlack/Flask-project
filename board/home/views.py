from flask import render_template
from . import index_bp
from ..models import Product


@index_bp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)
