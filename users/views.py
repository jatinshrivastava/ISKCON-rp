# # project/user/views.py
#
#
# #################
# #### imports ####
# #################
#
# from flask import render_template, Blueprint, url_for, \
#     redirect, flash, request
# from flask_login import login_user, logout_user, \
#     login_required, current_user
#
# from users.models import CustomUser
# # from project.email import send_email
# from iskcon import db, bcrypt
# from .forms import LoginForm, RegisterForm, ChangePasswordForm
#
#
# ################
# #### config ####
# ################
#
# user_blueprint = Blueprint('user', __name__,)
#
#
# ################
# #### routes ####
# ################
#
# @user_blueprint.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm(request.form)
#     if form.validate_on_submit():
#         user = CustomUser(
#             email=form.email.data,
#             password=form.password.data
#         )
#         db.session.add(user)
#         db.session.commit()
#
#         login_user(user)
#         flash('You registered and are now logged in. Welcome!', 'success')
#
#         return redirect(url_for('main.home'))
#
#     return render_template('user/register.html', form=form)
#
#
# @user_blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm(request.form)
#     if form.validate_on_submit():
#         user = CustomUser.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(
#                 user.password, request.form['password']):
#             login_user(user)
#             flash('Welcome.', 'success')
#             return redirect(url_for('main.home'))
#         else:
#             flash('Invalid email and/or password.', 'danger')
#             return render_template('user/login.html', form=form)
#     return render_template('user/login.html', form=form)
#
#
# @user_blueprint.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You were logged out.', 'success')
#     return redirect(url_for('user.login'))
#
#
# @user_blueprint.route('/profile', methods=['GET', 'POST'])
# @login_required
# def profile():
#     form = ChangePasswordForm(request.form)
#     if form.validate_on_submit():
#         user = CustomUser.query.filter_by(email=current_user.email).first()
#         if user:
#             user.password = bcrypt.generate_password_hash(form.password.data)
#             db.session.commit()
#             flash('Password successfully changed.', 'success')
#             return redirect(url_for('user.profile'))
#         else:
#             flash('Password change was unsuccessful.', 'danger')
#             return redirect(url_for('user.profile'))
#     return render_template('user/profile.html', form=form)

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from users.forms import SignUpForm
from .backends import MobilePhoneOrEmailModelBackend
import uuid


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone_number')
            raw_password = form.cleaned_data.get('password1')
            user = MobilePhoneOrEmailModelBackend.authenticate(None, request, username=email, password=raw_password)
            login(request, user)
            return redirect("chapter_index")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
