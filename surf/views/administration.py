# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for
from surf.form import ContactForm, Checkout, RegistrationForm, AddRoom, Addpost, Moreevent
from surf.database import User, RolesUsers, Role, User, Room, Event, Blog, Contact, Checkout, db_session, init_db
from sqlalchemy.orm import subqueryload
from sqlalchemy import desc


administration = Blueprint('administration', __name__, url_prefix='/administration')
@login_required
@administration.route('/', methods=['GET', 'POST'])
def index():
	#form = IndexForm()

	return render_template('/administration/index.html', title='Administration Panel')
##############################################################################################################""
@login_required
@administration.route('/rooms', methods=['GET', 'POST'])
def rooms():
	context = {'foo': 'bar'}


	rooms = Room.query.order_by(desc(Room.id)).limit(5)
	
	return render_template('/administration/rooms.html', context=context, rooms=rooms, title='Rooms of Hotel')

@login_required
@administration.route('/addroom', methods=['GET', 'POST'])
def addroom():
	form = AddRoom()
	if form.validate_on_submit():

		room = Room(title=form.title.data,description=form.description.data,price=form.price.data,mode=form.mode.data,home_img=form.home_img.data,img1_url=form.img1_url.data,img2_url=form.img2_url.data,img3_url=form.img3_url.data)


		db_session.add(room)
		db_session.commit()

		flash('Room Added seccussfly ;) .', 'success')

		# redirect to the login page
		return redirect(url_for('administration.addroom'))

	return render_template('/administration/addroom.html', form=form, title='Add Room', legend='Add Post')

@login_required
@administration.route('/<int:room_id>/updatroom', methods=['GET', 'POST'])
def updatroom(room_id):

	room = Room.query.get(room_id)
	form = AddRoom()

	if form.validate_on_submit():

		room.title = form.title.data
		room.description = form.description.data
		room.price = form.price.data
		room.home_img = form.home_img.data
		room.img1_url = form.img1_url.data
		room.img2_url = form.img2_url.data
		room.img3_url = form.img3_url.data

		db_session.commit()

		flash('Your Room Has been Updated !', 'success')
		return redirect(url_for('administration.rooms', room_id=room.id))

	elif request.method == 'GET':

		form.title.data = room.title
		form.description.data = room.description
		form.price.data = room.price
		form.home_img.data = room.home_img
		form.img1_url.data = room.img1_url
		form.img2_url.data = room.img2_url
		form.img3_url.data = room.img3_url

	return render_template('/administration/addroom.html', form=form, title='Update Room', legend='Update Post')

@login_required
@administration.route('/reservations/delroom/<int:id>', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def delete_room(id):
	"""
	Delete a department from the database
	"""
	#check_admin()

	room = Room.query.get(id)
	db_session.delete(room)
	db_session.commit()
	flash('You have successfully delete Room.', "success")

	# redirect to the departments page
	return redirect(url_for('administration.rooms'))

	return render_template(title="Delete Room")

###########################################################################################################
@login_required
@administration.route('/users', methods=['GET', 'POST'])
def users():

	users = User.query.order_by(desc(User.id)).limit(5)

	return render_template('/administration/users.html', users=users, title='Users')


################################################# MESSAGE AREA ############################################################

@login_required
@administration.route('/messages', methods=['GET', 'POST'])
def messages():

	contacts = Contact.query.order_by(desc(Contact.id)).limit(5)


	return render_template('/administration/messages.html', contacts=contacts, title='Inbox')

@login_required
@administration.route('/messages/show/<id_slug:contact_id>', methods=['GET', 'POST'])
def showmsg(contact_id):

	#checkouts = Checkout.query.all()
	#checkouts = Checkout.query.order_by(desc(Checkout.id)).limit(5)

	contacts = Contact.query.filter_by(id=contact_id).one()

	url_for('administration.showmsg', contact_id=contacts)

	#form = Addpost()

	return render_template('/administration/show_message.html', contacts=contacts, title='Open Message')

@login_required
@administration.route('/messages/delete/<int:id>', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def delete_msg(id):
	"""
	Delete a department from the database
	"""
	#check_admin()

	contacts = Contact.query.get(id)
	db_session.delete(contacts)
	db_session.commit()
	flash('You have successfully delete Message.', "success")

	# redirect to the departments page
	return redirect(url_for('administration.messages'))

	return render_template(title="Delete Message")
########################################### BLOG AREA ###############################################################

@login_required
@administration.route('/blog', methods=['GET', 'POST'])
def blog():

	#blogs = Blog.query.all()
	blogs = Blog.query.order_by(desc(Blog.id)).limit(5)

	return render_template('/administration/blog.html', blogs=blogs, title='Blog')

@administration.route('/blog/addpost', methods=['GET', 'POST'])
def addpost():

	form = Addpost()
	if form.validate_on_submit():

		blogs = Blog(title=form.title.data,body=form.body.data,img_off=form.img_off.data,tags=form.tags.data)


		db_session.add(blogs)
		db_session.commit()

		flash('Post Added seccussfly ;) .', 'success')

		# redirect to the login page
		return redirect(url_for('administration.addpost'))

	return render_template('/administration/addpost.html', form=form, title='New Post', legend='Add Post')

@login_required
@administration.route('/blog/delete/<int:id>', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def delete_blog(id):
	"""
	Delete a department from the database
	"""
	#check_admin()

	blogs = Blog.query.get(id)
	db_session.delete(blogs)
	db_session.commit()
	flash('You have successfully delete Post.', "success")

	# redirect to the departments page
	return redirect(url_for('administration.blog'))

	return render_template(title="Delete Post")

@login_required
@administration.route('/updatblog/<int:blogs_id>/', methods=['GET', 'POST'])
def updatblog(blogs_id):

	blogs = Blog.query.get(blogs_id)
	form = Addpost()

	if form.validate_on_submit():

		blogs.title = form.title.data
		blogs.img_off = form.img_off.data
		blogs.body = form.body.data
		blogs.tags = form.tags.data


		db_session.commit()

		flash('Your Post Has been Updated !', 'success')
		return redirect(url_for('administration.blog', blogs_id=blogs.id))

	elif request.method == 'GET':

		form.title.data = blogs.title
		form.img_off.data = blogs.img_off
		form.body.data = blogs.body
		form.tags.data = blogs.tags


	return render_template('/administration/addpost.html', form=form, title='Update Post', legend='Update Post')


#################################################Reservation Area#################################################################

@login_required
@administration.route('/reservations', methods=['GET', 'POST'])
def reservations():

	#checkouts = Checkout.query.all()
	checkouts = Checkout.query.order_by(desc(Checkout.id)).limit(5)

	#form = Addpost()

	return render_template('/administration/reservation.html', checkouts=checkouts, title='Reservations')


@login_required
@administration.route('/reservations/<id_slug:checkout_id>', methods=['GET', 'POST'])
def showreserve(checkout_id):

	#checkouts = Checkout.query.all()
	#checkouts = Checkout.query.order_by(desc(Checkout.id)).limit(5)

	checkouts = Checkout.query.filter_by(id=checkout_id).one()

	url_for('administration.showreserve', checkout_id=checkouts)

	#form = Addpost()

	return render_template('/administration/show_reservation.html', checkouts=checkouts, title='Reservations')


@login_required
@administration.route('/reservations/delres/<int:id>', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def delete_reservation(id):
	"""
	Delete a department from the database
	"""
	#check_admin()

	checkouts = Checkout.query.get(id)
	db_session.delete(checkouts)
	db_session.commit()
	flash('You have successfully delete Reservation.', "success")

	# redirect to the departments page
	return redirect(url_for('administration.reservations'))

	return render_template(title="Delete Reservation")

##################################################################################################



#######################################################EVENT AREA ##################################################""
@login_required
@administration.route('/events', methods=['GET', 'POST'])
def events():

	#events = Event.query.all()
	events = Event.query.order_by(desc(Event.id)).limit(5)

	return render_template('/administration/events.html', events=events, title='Events')

@login_required
@administration.route('/events/addevent', methods=['GET', 'POST'])
def addevent():

	form = Moreevent()
	if form.validate_on_submit():

		events = Event(title=form.title.data,description=form.description.data,tags=form.tags.data,home_img=form.home_img.data)


		db_session.add(events)
		db_session.commit()

		flash('Event Added seccussfly ;) .', 'success')

		# redirect to the login page
		return redirect(url_for('administration.addevent'))


	

	return render_template('/administration/addevent.html', form=form, title='Add Event', legend='Add Event')
	
@login_required
@administration.route('/upevents/<int:events_id>/', methods=['GET', 'POST'])
def upevents(events_id):

	events = Event.query.get(events_id)
	form = Moreevent()

	if form.validate_on_submit():

		events.title = form.title.data
		events.description = form.description.data
		events.tags = form.tags.data
		events.home_img = form.home_img.data

		db_session.commit()

		flash('Your Events Has been Updated !', 'success')
		return redirect(url_for('administration.events', events_id=events.id))

	elif request.method == 'GET':

		form.title.data = events.title
		form.description.data = events.description
		form.tags.data = events.tags
		form.home_img.data = events.home_img

	return render_template('/administration/addevent.html', form=form, title='Update Event', legend='Update Event')

@login_required
@administration.route('/events/delenvent/<int:id>', methods=['GET', 'POST'])
#@login_required
#@roles_required('superadmin')
def delete_event(id):
	"""
	Delete a department from the database
	"""
	#check_admin()

	events = Event.query.get(id)
	db_session.delete(events)
	db_session.commit()
	flash('You have successfully delete Event.', "success")

	# redirect to the departments page
	return redirect(url_for('administration.events'))

	return render_template(title="Delete Event")