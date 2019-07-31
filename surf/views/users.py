# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for

from surf.form import LoginForm, RegistrationForm
from flask_security import login_user, current_user, logout_user, roles_required, Security, login_required, SQLAlchemySessionUserDatastore
from werkzeug.security import generate_password_hash, check_password_hash
from surf.database import User, RolesUsers, Role, User, Room, Event, Blog, Contact, db_session, init_db
#from flask_security import Security, login_required, SQLAlchemySessionUserDatastore, login_user, current_user, logout_user, login_required
from surf import login_manager

users = Blueprint('users', __name__, url_prefix='/users')


#session = db_session()

user_datastore = SQLAlchemySessionUserDatastore(db_session,
										User, Role)

security = Security(user_datastore)

@users.route('/login', methods=['GET', 'POST'])
def login():

	form = LoginForm()
	if form.validate_on_submit():

		# check whether Client exists in the database and whether
		# the password entered matches the password in the database
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(
				form.password.data):
			# log Client in
			login_user(user)

			# redirect to the dashboard page after login
			return redirect(url_for('main.index'))

		# when login details are incorrect
		else:
			flash("Invalid Email Or Password ..!", 'danger')

	
	return render_template('security/login.html', form=form, title='Sign in')



@users.route('/register', methods=['GET', 'POST'])
def register():

	form = RegistrationForm()
	if form.validate_on_submit():


		#user = User(F_name=form.F_name.data,L_name=form.L_name.data,city=form.city.data,state=form.state.data,zipcode=form.zipcode.data,addr=form.addr.data,password=form.password.data,phone=form.phone.data,email=form.email.data):
		user = User(email=form.email.data,username=form.username.data,password=form.password.data)
		#user.set_password(password=form.password.data)
		
		# add Client to the database
		db_session.add(user)
		db_session.commit()
		flash('You Are Now Registered Please Log in !', 'success')

		# redirect to the login page
		return redirect(url_for('users.login'))

	return render_template('security/register.html', form=form, title='Sign up')


@users.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
	logout_user()
	flash("You are now loggin out !!", 'success')
	return redirect(url_for('users.login'))