from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired

class Login(FlaskForm):
		username = StringField('USERNAME',validators=[DataRequired()])
		password = PasswordField('PASSWORD',validators=[DataRequired()])
		submit = SubmitField('Submit')
		remember = BooleanField('Remember Me')