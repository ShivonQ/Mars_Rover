from flask_wtf import Form
from wtforms.fields.html5 import DateField
from wtforms.widgets import RadioInput


class DateForm(Form):
    dt = DateField('DatePicker', format='%y-%m-%d')