from flasktodo.models import User, Lists
from flask import Flask, render_template, url_for, flash, redirect, request
from flasktodo.forms import RegistrationForm, LoginForm, AccountUpdate, ListForm
from flasktodo import app, db,  bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os


#pagination is not working, getting error that the pagination orbject is not iterable?
@app.route('/')
@app.route('/home')
def home():
    page = request.args.get('page', 1, type =int)
    lists= Lists.query.paginate( page=page, per_page=2)
    #lists= Lists.query.all()
    return render_template('home.html', lists = lists)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect (url_for('home'))
        else:
            flash('login unuccessful', 'danger')

    return render_template('login.html', title = 'Login', form =form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created, please log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _ , f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', picture_fn)

   

    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
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

@app.route("/list/new", methods=['GET', 'POST'])
@login_required
def new_list():
    form = ListForm()
    if form.validate_on_submit():
        list=Lists(title =form.title.data, content = form.content.data, user_id = current_user.get_id())
        db.session.add(list)
        db.session.commit()
        flash('New list has been created', 'success')
        return redirect(url_for('home'))
    return render_template('create_list.html', title ='New List', form = form,  legend= 'New Post')


@app.route("/list/<int:list_id>", methods=['GET', 'POST'])
@login_required
def list(list_id):
    lists =Lists.query.get_or_404(list_id)
    return render_template('list.html', title=lists.title, lists=lists)

@app.route("/list/<int:list_id>/update", methods=['GET', 'POST'])
@login_required
def update_list(list_id):
    lists =Lists.query.get(list_id)
    form = ListForm()
    if lists.user_id != current_user.get_id():
        abort(403)
    if form.validate_on_submit():
        lists.title = form.title.data
        lists.content = form.content.data
        db.session.commit()
        flash('Your list has been updated')
        return redirect(url_for('list', list_id = list_id))
        ##issue with this route  not working properly, redirectig to list page without showing the update form
    elif request.method == 'GET':
        form.title.data = lists.title
        form.content.data=lists.content  
    return render_template('create_list.html', title ='Update List', form = form, legend= 'Update Post' )


@app.route("/list/<int:list_id>/delete", methods=['POST'])
@login_required
def delete_list(list_id):
    list = Lists.query.get_or_404(list_id)
    db.session.delete(list)
    db.session.commit()
    flash('List has been deleted')
    return redirect(url_for('home'))