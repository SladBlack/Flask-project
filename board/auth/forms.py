from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(1, 32),
                                                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                  'Имя пользователя должно содержать только буквы, '
                                                                  'числа, точки или нижние подчеркивания')])
    password = PasswordField('Пароль', validators=[DataRequired(), EqualTo('password2',
                                                                           message='Пароли не совпадают')])
    password2 = PasswordField('Подтвердить пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email уже зарегистрирован')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Такой ник уже существует')
