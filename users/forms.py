# # project/user/forms.py
#
#
# from flask_wtf import FlaskForm
# from wtforms import TextField, PasswordField
# from wtforms.validators import DataRequired, Email, Length, EqualTo
#
# from users.models import CustomUser
#
#
# class LoginForm(FlaskForm):
#     email = TextField('email', validators=[DataRequired(), Email()])
#     password = PasswordField('password', validators=[DataRequired()])
#
#
# class RegisterForm(FlaskForm):
#     email = TextField(
#         'email',
#         validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
#     password = PasswordField(
#         'password',
#         validators=[DataRequired(), Length(min=6, max=25)]
#     )
#     confirm = PasswordField(
#         'Repeat password',
#         validators=[
#             DataRequired(),
#             EqualTo('password', message='Passwords must match.')
#         ]
#     )
#
#     def validate(self):
#         initial_validation = super(RegisterForm, self).validate()
#         if not initial_validation:
#             return False
#         user = CustomUser.query.filter_by(email=self.email.data).first()
#         if user:
#             self.email.errors.append("Email already registered")
#             return False
#         return True
#
#
# class ChangePasswordForm(FlaskForm):
#     password = PasswordField(
#         'password',
#         validators=[DataRequired(), Length(min=6, max=25)]
#     )
#     confirm = PasswordField(
#         'Repeat password',
#         validators=[
#             DataRequired(),
#             EqualTo('password', message='Passwords must match.')
#         ]
#     )

from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.constants import COUNTRY_CODES
from users.models import CustomUser
import uuid

import re


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)
    phone_number = forms.CharField(max_length=12, min_length=10)
    country_code = forms.CharField(widget=forms.Select(choices=COUNTRY_CODES), max_length=16, required=True, initial='+91')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'gender', 'birth_date', 'country_code', 'phone_number', 'address', 'country_name', 'password1', 'password2', )
        widgets = {
            'birth_date': DateInput(),
        }