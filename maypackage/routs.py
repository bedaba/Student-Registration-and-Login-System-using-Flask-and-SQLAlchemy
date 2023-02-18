# import flask
from maypackage import *
from maypackage.forms import RegistrationForm, LoginForm, SubjectForm
from maypackage.model import User, Post, Subject
from flask import request

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
def regesterform():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Save User
        try:
            with app.app_context():
                user = User(username=form.username.data, email=form.email.data, password=form.password.data)
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
        usersobj = User.query.all()
        username = form.username.data
        passwoed = form.password.data
        for user in usersobj:
            if username == user.username and passwoed == user.password:
                flash('You were successfully logged in', 'success')
                return redirect(url_for('home'))
        return render_template('login.html', form=form, error=1, title="Login Page")
    return render_template('login.html', form=form, title="Login PAge")


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
