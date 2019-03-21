from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# IN ANY FUNCTION ADDING TO THE DB REMEMBER TO INCLUDE SOMETHING TO CATCH
# INVALIDREQUESTERRORS AND ROLLBACK THE SESSION THEN TRY TO ADD AGAIN


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), index=True, unique=True)
    password = db.Column(db.String(45))
    email = db.Column(db.String(100))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    __tablename__ = 'posts'
    pid = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    date = db.Column(db.DateTime)
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    progid = db.Column(db.Integer)  # fk for saved progression

    def __repr__(self):
        return '<Post {}>'.format(self.content)


class Chord(db.Model):
    __tablename__ = 'chords'
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True)
    image = db.Column(db.String(100))

    def __repr__(self):
        return '<Chord {}>'.format(self.name)


class KeyChord(db.Model):
    __tablename__ = 'keychords'
    kid = db.Column(db.Integer, db.ForeignKey('`keys`.kid'))
    cid = db.Column(db.Integer, db.ForeignKey('chords.cid'))

    def __repr__(self):
        return '<keychords {}>'.format(self.kid, self.cid)


class Key(db.Model):
    __tablename__ = '`keys`'
    kid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True)


class Progression(db.Model):
    __tablename__ = 'progressions'
    progid = db.Column(db.Integer, primary_key=True)
    c1 = db.Column(db.Integer, db.ForeignKey('chords.cid'))
    c2 = db.Column(db.Integer, db.ForeignKey('chords.cid'))
    c3 = db.Column(db.Integer, db.ForeignKey('chords.cid'))
    c4 = db.Column(db.Integer, db.ForeignKey('chords.cid'))
    date = db.Column(db.DateTime)
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))