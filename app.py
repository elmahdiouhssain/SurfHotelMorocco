from surf import app
import os
#from surf.database import db_session
from flask import Flask, session, g, render_template
from datetime import datetime
#from flask_security import Security, login_user, current_user
from surf.database import User, RolesUsers, Role, User, Room, Checkout, Event, Blog, Contact, db_session, init_db

# Register the blueprints
from surf.views import main
app.register_blueprint(main.main)

from surf.views import users
app.register_blueprint(users.users)

from surf.views import rooms
app.register_blueprint(rooms.rooms)

from surf.views import blog
app.register_blueprint(blog.blog)


from surf.views import administration
app.register_blueprint(administration.administration)


@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Blog': Blog, 'Room': Room, 'Checkout': Checkout}


#@app.errorhandler(404)
#def not_found(error):
  #return render_template('404.html'), 404
