from app import app, db
from flask import render_template, flash, redirect
from app.forms import LoginForm, SignupForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return "Chordy: an application"


# This requires the usage of an html form for what the login page
# looks like. It so far only has username, password, and sign in
# functions but it is easy to add more
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return '/index'  # need to add a function to grab urls
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # do something here to grab the uid from the DB as well
        # maybe dont need because the user instance already has the uid in it?
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return '/login'  # same as before
        login_user(user)
        return '/index'  # same as before
    return render_template(login.html, title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return '/login'  # still need something to grab redirect urls


@app.route('/signup', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return '/index'  # yep
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registered')
        return '/login'  # yep
    return render_template('signup.html', title='Sign Up', form=form)  # Need a signup template

