from flask import Blueprint, flash, redirect, url_for, render_template, request
from flask_login import login_user, login_required, logout_user, current_user

from flaskBlog import bcrypt, db
from flaskBlog.models import User, Post
from flaskBlog.users.forms import RegistrationForm, LoginForm, UpdateProfileForm, RequestResetForm, ResetPasswordForm
from flaskBlog.users.utils import save_profile_pic, send_email

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_passwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_passwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account created successfully. Please login !!! ', category='success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title="Registration", form=form)


@users.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # if form.email.data == 'tej@gmail.com' and form.password.data == 'tej':
        #     flash(f'Logged in as {form.email.data} !!! ', category='success')
        #     return redirect(url_for('home'))
        # else:
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.rememberMe.data)
            next_page = request.args.get('next')
            flash(f'Logged in as {user.username} !!! ', category='success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Login failed', category='danger')
    return render_template('login.html', title="Login", form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.image.data:
            pic = save_profile_pic(form.image.data)
            current_user.image = pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your account updated successfully. !!! ', category='success')
        return redirect(url_for('users.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename='pics/' + current_user.image)
    return render_template('profile.html', title="Profile", image=image, form=form)



@users.route('/reset_password', methods=['POST', 'GET'])
def request_token():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_email(user)
        flash('Email sent successfully to reset password. Please check it.', 'success')
        return redirect(url_for('users.request_token'))
    return render_template('request_token.html', title='Reset Password Request', form=form)


@users.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_password(token):
    user = User.verify_token(token)
    if user is None:
        flash('Invalid or expired token', 'warning')
        return redirect(url_for('users.request_token'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_passwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_passwd
        db.session.commit()
        flash(f'Your password changed successfully. Please login !!! ', category='success')
        return redirect(url_for('users.login'))

    return render_template('reset_password.html', title='Reset Password', form=form)
