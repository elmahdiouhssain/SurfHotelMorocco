# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for

from surf.form import ContactForm, GetRoom, RegistrationForm, AddRoom, Addpost, Moreevent
from surf.database import User, RolesUsers, Role, User, Room, Event, Blog, Contact, Checkout, db_session, init_db
from sqlalchemy.orm import subqueryload
from sqlalchemy import desc

rooms = Blueprint('rooms', __name__, url_prefix='/rooms')


@rooms.route('/show/<id_slug:room_id>', methods=['GET', 'POST'])
def room(room_id):

	#checkouts = Checkout.query.all()
	#checkouts = Checkout.query.order_by(desc(Checkout.id)).limit(5)

	rooms = Room.query.filter_by(id=room_id).one()

	url_for('rooms.room', room_id=rooms)


	return render_template('/room_details.html', rooms=rooms, title='Show Details')




@rooms.route('/available', methods=['GET', 'POST'])
def available():

	context = {'foo': 'bar'}


	rooms = Room.query.order_by(desc(Room.id)).limit(5)

	#rooms = Room.query(Room).filter(Room.mode == "OPENED")
	#rooms = Room.query(Room).filter(Room.mode == 'OPENED')

	#form = Checkout()

	return render_template('/ra.html', rooms=rooms,  title='Available Rooms')


@rooms.route('/booknow/<id_slug:room_id>', methods=['GET', 'POST'])
def getroom(room_id):

	rooms = Room.query.filter_by(id=room_id).one()

	url_for('rooms.getroom', room_id=rooms)

	che = GetRoom()
	if che.validate_on_submit():
		pst = Checkout(fullname=che.fullname.data,email=che.email.data,city=che.city.data,state=che.state.data,phone=che.phone.data,zipcode=che.zipcode.data,addr=che.addr.data)
		#user.set_password(password=form.password.data)
		
		# add Client to the database
		db_session.add(pst)
		db_session.commit()
		flash('You are now complete reservation !', 'success')

		# redirect to the login page
		return redirect(url_for('rooms.getroom', room_id=rooms))




	return render_template('/getroom.html', che=che, rooms=rooms, title='Book This Room')

