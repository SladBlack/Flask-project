from flask import render_template, flash, url_for, redirect, request
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index_bp.index')
            return redirect(next)
        flash('Неверное имя пользователя или пароль')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password_hash=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Аккаунт создан')
        return redirect(url_for('index_bp.index'))
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта')
    return redirect(url_for('index_bp.index'))
