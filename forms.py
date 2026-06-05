from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, SubmitField, SelectField, PasswordField
from wtforms import validators, ValidationError
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

class LinkForm(FlaskForm):
  url = StringField("Link",  [validators.DataRequired()])
