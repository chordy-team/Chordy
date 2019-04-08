from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SignupForm, ChordGenForm, SavedChordsForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Progression, Chord
from datetime import datetime


@app.route('/')
def default():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = ChordGenForm()
    if form.chord1.data:
        user = current_user
        progression = Progression(c1 = Chord.query.filter_by(name=form.chord1.data).first().cid, 
            c2 = Chord.query.filter_by(name=form.chord2.data).first().cid, 
            c3 = Chord.query.filter_by(name=form.chord3.data).first().cid, 
            c4 = Chord.query.filter_by(name=form.chord4.data).first().cid, 
            date = datetime.now(), 
            uid = user.uid)
        db.session.add(progression)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('home.html', title='Home', form=form)

@app.route('/chords', methods=['GET', 'POST'])
@login_required
def chordsList():
    form = SavedChordsForm()
    progressions = Progression.query.filter_by(uid=current_user.uid).all()
    progs = []
    i = 0
    for prog in progressions:
        progs.append([])
        progs[i] = ([Chord.query.filter_by(cid=prog.c1).first().name, 
            Chord.query.filter_by(cid=prog.c2).first().name, 
            Chord.query.filter_by(cid=prog.c3).first().name, 
            Chord.query.filter_by(cid=prog.c4).first().name,
            prog.progid])
        i = i + 1
    if form.is_submitted():
        toDelete = Progression.query.filter_by(progid=form.progid.data).first()
        app.logger.info(toDelete)
        db.session.delete(toDelete)
        db.session.commit()
        return redirect(url_for('chordsList'))
    return render_template('chordsList.html', form = form, title='Saved Chords', progs = progs)

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
        if user is None or not user.check_password(form.password.data):
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
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Sucessfully Signed Up')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)  # Need a signup template