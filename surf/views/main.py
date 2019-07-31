# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for

from surf.form import ContactForm, GetRoom, RegistrationForm, AddRoom, Addpost, Moreevent, Available
from surf.database import User, RolesUsers, Role, User, Room, Event, Blog, Contact, Checkout, db_session, init_db
from sqlalchemy.orm import subqueryload
from sqlalchemy import desc


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
	form = Available()

	rooms = Room.query.order_by(desc(Room.id)).limit(5)

	blogs = Blog.query.order_by(desc(Blog.id)).limit(2)

	events = Event.query.order_by(desc(Event.id)).limit(2)


	return render_template('/index.html', form=form, rooms=rooms, blogs=blogs, events=events, title='Tamraght Surf Hotel')


@main.route('/about-us')
def about():

	return render_template('/about.html', title='About')


@main.route('/accommodation')
def accomodation():

	rooms = Room.query.order_by(desc(Room.id)).limit(9)


	return render_template('/accomodation.html', rooms=rooms, title='Accomodation')

@main.route('/surf-spots')
def surf():

	return render_template('/surf.html', title='Surf')

@main.route('/our-packs')
def packages():

	return render_template('/pack.html', title='Packages')

@main.route('/surf-coaching/')
def surfcoaching():

	#form = ContactForm()

	return render_template('/surf_coaching.html', title='Surf Coaching')

@main.route('/surf-guiding')
def surfguiding():

	#form = ContactForm()

	return render_template('/surf_guiding.html', title='Surf Guiding')

@main.route('/surf-yoga')
def surfyoga():

	#form = ContactForm()

	return render_template('/surf_yoga.html', title='Surf & Yoga')

@main.route('/activities')
def activities():

	return render_template('/activities.html', title='Activities')

@main.route('/contact')
def contact():

	form = ContactForm()

	return render_template('/contact.html', form=form, title='Contact Us')



@main.route('/agadir')
def agadir():

	#form = ContactForm()

	return render_template('/act/agadir.html', title='Agadir')

@main.route('/surfing')
def surfing():

	#form = ContactForm()

	return render_template('/act/surf.html', title='Surfing')


@main.route('/yoga')
def yoga():

	#form = ContactForm()

	return render_template('/act/yoga.html', title='Yoga')

@main.route('/hammam-and-massage')
def hammas():

	#form = ContactForm()

	return render_template('/act/hammam.html', title='Hammam & Massage')

@main.route('/quad')
def quad():

	#form = ContactForm()

	return render_template('/act/quad.html', title='Quad')

@main.route('/horse')
def horse():

	#form = ContactForm()

	return render_template('/act/horse.html', title='Horse')

@main.route('/paradise')
def paradise():

	#form = ContactForm()

	return render_template('/act/paradise.html', title='Paradise')

@main.route('/the-bay-of-imessouane')
def imswan():

	#form = ContactForm()

	return render_template('/act/imswane.html', title='the-bay-of-imessouane')

@main.route('/essaouira')
def essaouira():

	#form = ContactForm()

	return render_template('/act/essaouira.html', title='Essaouira')

@main.route('/marrakech')
def marrakech():

	#form = ContactForm()

	return render_template('/act/marrakesh.html', title='Marrakech')