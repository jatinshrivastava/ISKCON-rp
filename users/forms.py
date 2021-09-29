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
from django.contrib.auth.forms import AuthenticationForm
import uuid

import re


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control w-50'}))
    phone_number = forms.CharField(max_length=12, min_length=10, widget=forms.TextInput(attrs={'class': 'form-control w-50'}))
    country_code = forms.CharField(widget=forms.Select(choices=COUNTRY_CODES, attrs={'class': 'form-control w-50'}), max_length=16, required=True, initial='+91')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'gender', 'birth_date', 'country_code', 'phone_number', 'address', 'country_name', 'password1', 'password2', )
        widgets = {
            'birth_date': DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'country_name': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
))