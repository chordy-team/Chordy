from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SignupForm, ChordGenForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/')
def default():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/index')
@login_required
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ChordGenForm()
    return render_template('home.html', title='Home', form=form)

@app.route('/chords')
def chordsList():
    return render_template('chordsList.html', title='Saved Chords')

# This requires the usage of an html form for what the login page
# looks like. It so far only has username, password, and sign in
# functions but it is easy to add more
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # uid = user.query.filter_by(username=user.username.uid).first()  # I have no idea if this works but it should grad the uid of the user?
        if user is None or user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('loginpage.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logoutfunct():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signupfunct():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, email=form.email.data)
        # user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Sucessfully Signed Up')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)  # Need a signup template