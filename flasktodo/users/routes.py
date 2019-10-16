from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flasktodo import db, bcrypt
from flasktodo.models import User, Lists
from flasktodo.users.forms import (RegistrationForm, LoginForm, AccountUpdate,)


users= Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect (url_for('main.home'))
        else:
            flash('login unuccessful', 'danger')

    return render_template('login.html', title = 'Login', form =form)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created, please log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))



@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = AccountUpdate()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file 
        current_user.username= form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account updated', 'success')
        return redirect(url_for('account'))
    elif request.method =='get':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pictures/'+ current_user.image_file)
    return render_template('account.html', title='Your Profile', image_file = image_file, form = form)