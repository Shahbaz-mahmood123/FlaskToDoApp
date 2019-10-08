from flasktodo.models import User, Lists
from flask import Flask, render_template, url_for, flash, redirect
from flasktodo.forms import RegistrationForm, LoginForm
from flasktodo import app, db,  bcrypt

posts = [
    {
        'user': 'Shahbaz Mahmood',
        'title': 'List1',
        'content': 'first todo list',
        'date_created': 'today',
    },

    {
        'user': 'test test',
        'title': 'test',
        'content': 'test todo list',
        'date_osted': 'yesterday',  
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='test@test.com' and form.password.data =='password':
            flash('Log in succesufull', 'success')
        return redirect(url_for('home'))
    else:
        flash('login unuccessful', 'danger')
    return render_template('login.html', title = 'Login', form =form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created, please log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)