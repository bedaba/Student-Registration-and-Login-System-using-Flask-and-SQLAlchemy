# import flask

from maypackage import *

from flask_bcrypt import generate_password_hash, check_password_hash
from flask import flash, request

from maypackage import app, db
from maypackage.forms import RegistrationForm, LoginForm, SubjectForm
from maypackage.model import User, Post, Subject
from flask_login import login_user, current_user, logout_user
from test import create_db


@app.route('/')
def home():
    nav = {
        'home': "/",
        'about': "about",
        'navfromHome': "#",
    }
    create_db()
    return render_template('index.html', nav=nav, title="home")


@app.route('/about')
def about():
    nav = {
        'home': "/",
        'about': "about",
        'navfromAbout': "#",
    }
    return render_template('abouts.html', nav=nav, title="about")

@app.route('/Registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            error = "Email is already taken"
            return render_template('Registration.html', form=form, title="Registration Form", error=error)

        hashed_password = generate_password_hash(form.password.data).decode('utf-8')
        try:
            with app.app_context():
                user = User(username=form.username.data, email=form.email.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
        except Exception as e:
            return render_template('Registration.html', form=form, title="Registration Form", error=e)
        return redirect(url_for('login'))
    return render_template('Registration.html', form=form, title="Registration Form")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You were successfully logged in', 'success')
            return redirect(url_for('home'))
        flash('Login Unsuccessful. Please check email and password', 'danger')
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('login.html', form=form, title="Login Page")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/subjects', methods=['GET', 'POST'])
def subject_Add():
    form = SubjectForm()
    if form.title.data:
        users = request.form.get('users')
        for userId in users:
            with app.app_context():
                subjectobj = Subject(title=form.title.data, details=form.details.data, user_id=userId)
                db.session.add(subjectobj)
                db.session.commit()
        user = User.query.filter_by(id=userId).first()
        print(user.subjects)
    usersobj = User.query.all()
    return render_template('subjectAdd.html', form=form, usersobj=usersobj, title="subject_Add Form")
