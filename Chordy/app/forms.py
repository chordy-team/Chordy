from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-enter Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  # this queries db to see if the username already exists
        if user is not None:
            raise ValidationError('username already taken')


class ChordGenForm(FlaskForm):
    # chord1 = TextAreaField('chord1', validators=[DataRequired()])
    # chord2 = TextAreaField('chord2', validators=[DataRequired()])
    # chord3 = TextAreaField('chord3', validators=[DataRequired()])
    # chord4 = TextAreaField('chord4', validators=[DataRequired()])
    # num1 = TextAreaField('num1', validators=[DataRequired()])
    # num2 = TextAreaField('num2', validators=[DataRequired()])
    # num3 = TextAreaField('num3', validators=[DataRequired()])
    # num4 = TextAreaField('num4', validators=[DataRequired()])
    # keySelect = SelectField('Languages', choices=[('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('A', 'A'), ('B', 'B')])
    # submit = SubmitField('Save')
    chord1 = StringField('chord1')
    chord2 = StringField('chord2')
    chord3 = StringField('chord3')
    chord4 = StringField('chord4')
    num1 = StringField('num1')
    num2 = StringField('num2')
    num3 = StringField('num3')
    num4 = StringField('num4')
    keySelect = SelectField('Languages',
                            choices=[('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('A', 'A'),
                                     ('B', 'B')])
    submit = SubmitField('Save')


class TestForm(FlaskForm):
    chord1 = StringField("First Chord", validators=[DataRequired()])
    chord2 = StringField("Second Chord", validators=[DataRequired()])
    chord3 = StringField("Third Chord", validators=[DataRequired()])
    chord4 = StringField("Fourth Chord", validators=[DataRequired()])
    submit = SubmitField('Save')


class EditForm(FlaskForm):
    chord1 = StringField("First", validators=[DataRequired()])
    chord2 = StringField("Second", validators=[DataRequired()])
    chord3 = StringField("Third", validators=[DataRequired()])
    chord4 = StringField("Fourth", validators=[DataRequired()])
    submit = SubmitField('Submit')


class RandomForm(FlaskForm):
    keyChoices = [(5, 'Amaj'), (7, 'Bmaj'), (9, 'C#maj'), (2, 'Cmaj'), (4, 'Dmaj'), (6, 'Emaj'), (8, 'F#maj'), (3, 'Gmaj')]
    chosenKey = SelectField("Choose A Key", choices=keyChoices)
    submit = SubmitField('Generate Chords')
