import os
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'hello-there'
    SECRET_KEY = 'hello-there'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or\
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:MySQL@localhost:3306/mydb'  # this is where the location of the db is passed in
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
