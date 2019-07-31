from flask import Flask, g, session, render_template, make_response
from flask_bootstrap import Bootstrap
from surf.database import User, RolesUsers, Role, Room, Event, Checkout, Blog, Contact, db_session, init_db
from surf.form import Checkout, LoginForm, RegistrationForm, ContactForm, AddRoom, Moreevent
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore, login_user, current_user, logout_user, login_required
from flask_login import LoginManager, AnonymousUserMixin, UserMixin
from datetime import datetime, timedelta
from flask_wtf.recaptcha import RecaptchaField

from werkzeug.routing import BaseConverter
from inflection import parameterize
import sys

#from flask_migrate import Migrate
#import pymysql
sys.setrecursionlimit(1500)


app = Flask(__name__)
Bootstrap(app)


#Login manager configurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.session_protection = "strong"

# db variable initialization
db = SQLAlchemy()
#migrate = Migrate(app, db)

# keys for localhost. Change as appropriate.
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfU0HQUAAAAABo5PdJOvuUdmEw5h9lriU_C5kvQ'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfU0HQUAAAAAFq5emkzzktWjt5N7tgwXcOmGtH9'

# The real#
#app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfhzXQUAAAAAPIONTyhOc27VZrfwmVjh-9SxKG0'
#app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfhzXQUAAAAADu8B9086Fiyyv-KZrQCnBmSpQyo'

app.config['SECRET_KEY'] = 'b951cbe3a050f545c7d576d51312bb3eef39100f64ba5c718'
app.config['WTF_CSRF_SECRET_KEY'] = 'b951cbe3a0sdhjkjklsj98lks50f545c7d576d51312bb3eef39100f64ba5c718'

# Set config values for Flask-Security.
# We're using PBKDF2 with salt.
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
app.config['SECURITY_PASSWORD_SALT'] = 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
app.config['SECURITY_REGISTERABLE'] = True	
app.config['SECURITY_TRACKABLE'] = True
app.config['SECURITY_LOGIN_URL'] = '/security/login.html'
app.config['SECURITY_REGISTER_URL'] = '/security/register.html'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test2:test2@localhost/test2?charset=utf8mb4&binary_prefix=true'


# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session,
										User, Role)
security = Security(app, user_datastore)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class IDSlugConverter(BaseConverter):
    """Matches an int id and optional slug, separated by "/".

    :param attr: name of field to slugify, or None for default of str(instance)
    :param length: max length of slug when building url
    """

    regex = r'-?\d+(?:/[\w\-]*)?'

    def __init__(self, map, attr='title', length=80):
        self.attr = attr
        self.length = int(length)
        super(IDSlugConverter, self).__init__(map)

    def to_python(self, value):
        id, slug = (value.split('/') + [None])[:2]
        return int(id)

    def to_url(self, value):
        raw = str(value) if self.attr is None else getattr(value, self.attr, '')
        slug = parameterize(raw)[:self.length].rstrip('-')
        return '{}/{}'.format(value.id, slug).rstrip('/')



app.url_map.converters['id_slug'] = IDSlugConverter

if __name__ == '__main__':
	#app.run()
  app.run(host='0.0.0.0', debug=True)