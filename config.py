import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    STRIPE_PUB_KEY = 'pk_test_lGXe3xx2KfcxVMohkNhLQLzn00f0OXjTw8'
    STRIPE_SECRET_KEY = 'sk_test_lKL5mpbIp5XQh3X750dAA8yr00laScgXRm'