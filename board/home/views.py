from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user

from . import index_bp
from ..models import Product
from .forms import AddProductForm
from .. import db


@index_bp.route('/')
def index():
    products = Product.query.all()
    return render_template('home/index.html', products=products)


@index_bp.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        product = Product(user_id=current_user.id,
                          name=form.name.data,
                          price=form.price.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('index_bp.index'))
    return render_template('home/add_product.html', form=form)


@index_bp.route('/update_product/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.get_or_404(id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('home/update_product.html', product=product)


@index_bp.route('/delete_product/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    product_to_delete = Product.query.get_or_404(id)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
