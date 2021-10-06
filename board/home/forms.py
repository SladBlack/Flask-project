from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length


class AddProductForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired(), Length(1, 64)])
    price = DecimalField('Цена', validators=[DataRequired()])
    submit = SubmitField('Добавить')
