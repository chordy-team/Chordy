from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, SignupForm, TestForm, EditForm, RandomForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Chord, Progression, KeyChord, Key
import random


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = TestForm()
    selectform = RandomForm()
    if form.validate_on_submit():
        c1 = form.chord1.data
        c2 = form.chord2.data
        c3 = form.chord3.data
        c4 = form.chord4.data
        ch1 = Chord.query.filter_by(name=c1).first()
        ch2 = Chord.query.filter_by(name=c2).first()
        ch3 = Chord.query.filter_by(name=c3).first()
        ch4 = Chord.query.filter_by(name=c4).first()
        uid = current_user.id
        prog = Progression(c1=ch1.cid, c2=ch2.cid, c3=ch3.cid, c4=ch4.cid, uid=uid)
        db.session.add(prog)
        db.session.commit()
        flash("Saved Chord Progression!")
        return redirect(url_for('chordsList'))
    return render_template('testhome.html', title='Home', form=form, form2=selectform)


@app.route('/genchords/<val>', methods=['GET', 'POST'])
def genchords(val):
    form = TestForm()
    selectform = RandomForm()
    if request.method == 'GET':
        chords = KeyChord.query.filter_by(kid=val).all()
        returnchords = []
        while len(returnchords) <= 4:
            rand = random.choice(chords)
            returnchords.append(rand.cid)
        fchord = Chord.query.filter_by(cid=returnchords[0]).first()
        form.chord1.data = fchord.name
        schord = Chord.query.filter_by(cid=returnchords[1]).first()
        form.chord2.data = schord.name
        tchord = Chord.query.filter_by(cid=returnchords[2]).first()
        form.chord3.data = tchord.name
        fchord = Chord.query.filter_by(cid=returnchords[3]).first()
        form.chord4.data = fchord.name
    if form.validate_on_submit():
        c1 = form.chord1.data
        c2 = form.chord2.data
        c3 = form.chord3.data
        c4 = form.chord4.data
        ch1 = Chord.query.filter_by(name=c1).first()
        ch2 = Chord.query.filter_by(name=c2).first()
        ch3 = Chord.query.filter_by(name=c3).first()
        ch4 = Chord.query.filter_by(name=c4).first()
        uid = current_user.id
        progr = Progression(c1=ch1.cid, c2=ch2.cid, c3=ch3.cid, c4=ch4.cid, uid=uid)
        db.session.add(progr)
        db.session.commit()
        flash("Saved Chord Progression!")
        return redirect(url_for('chordsList'))
    return render_template('testhome.html', title='Home', form=form, form2=selectform)


@app.route('/chords', methods=['GET', 'POST'])
def chordsList():
    progressions = Progression.query.filter_by(uid=current_user.id).all()
    names = []
    for progression in progressions:
        prognames = []
        prognames.append(progression.progid)
        chord = Chord.query.filter_by(cid=progression.c1).first()
        prognames.append(chord.name)
        chord = Chord.query.filter_by(cid=progression.c2).first()
        prognames.append(chord.name)
        chord = Chord.query.filter_by(cid=progression.c3).first()
        prognames.append(chord.name)
        chord = Chord.query.filter_by(cid=progression.c4).first()
        prognames.append(chord.name)
        names.append(prognames)
    return render_template('chordsList.html', title='Saved Chords', progarray=names)


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
    return render_template('loginpage.html', title='Sign In', form=form, user=False)


@app.route('/logout', methods=['GET', 'POST'])
# @login_required
def logoutfunct():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signupfunct():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, email=form.email.data)
        # user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Sucessfully Signed Up')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/editprog/<editid>', methods=['GET', 'POST'])
def editprog(editid):
    prog = Progression.query.get(editid)
    form = EditForm()
    if request.method == 'GET':
        chord1 = Chord.query.filter_by(cid=prog.c1).first()
        form.chord1.data = chord1.name
        chord2 = Chord.query.filter_by(cid=prog.c2).first()
        form.chord2.data = chord2.name
        chord3 = Chord.query.filter_by(cid=prog.c3).first()
        form.chord3.data = chord3.name
        chord4 = Chord.query.filter_by(cid=prog.c4).first()
        form.chord4.data = chord4.name
    if form.validate_on_submit():
        c1 = form.chord1.data
        c2 = form.chord2.data
        c3 = form.chord3.data
        c4 = form.chord4.data
        ch1 = Chord.query.filter_by(name=c1).first()
        ch2 = Chord.query.filter_by(name=c2).first()
        ch3 = Chord.query.filter_by(name=c3).first()
        ch4 = Chord.query.filter_by(name=c4).first()
        prog.c1 = ch1.cid
        prog.c2 = ch2.cid
        prog.c3 = ch3.cid
        prog.c4 = ch4.cid
        db.session.commit()
        return redirect(url_for('chordsList'))
    return render_template('edit.html', title='Edit Progression', form=form, progression=prog)


@app.route('/deleteprog/<deleteid>', methods=['GET', 'POST'])
def deleteprog(deleteid):
    prog = Progression.query.filter_by(progid=deleteid).first()
    db.session.delete(prog)
    db.session.commit()
    return redirect(url_for('chordsList'))
