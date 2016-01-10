from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired



class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    openid2 = StringField('openid2', validators=[DataRequired()])