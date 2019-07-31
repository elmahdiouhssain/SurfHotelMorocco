from datetime import datetime
from sqlalchemy import create_engine, Column, TEXT, Integer, String, Boolean, DateTime, \
	 ForeignKey, event

from flask import flash, g, jsonify

from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship, subqueryload

from sqlalchemy.ext.declarative import declarative_base

from flask import url_for, Markup

from flask_security import UserMixin, RoleMixin, SQLAlchemySessionUserDatastore, Security
from werkzeug.security import generate_password_hash, check_password_hash


#from mysql.connector import (connection)
import os
from flask_login import LoginManager
import pymysql

login_manager = LoginManager()

engine = create_engine('mysql+pymysql://ss00:ss00@localhost/ss00?charset=utf8mb4&binary_prefix=true')

#mysql+pymysql://acomplexbc:acomplexbc@localhost/acomplexbc?charset=utf8mb4&binary_prefix=true

db_session = scoped_session(sessionmaker(autocommit=False,
										 autoflush=False,
										 bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
Model.query = db_session.query_property()

#Stop the connection to db
#cnx.close()

class RolesUsers(Base):

	__tablename__ = 'roles_users'
	id = Column(Integer(), primary_key=True)
	user_id = Column('user_id', Integer(), ForeignKey('user.id'))
	role_id = Column('role_id', Integer(), ForeignKey('role.id'))

class Role(Base, RoleMixin):

	__tablename__ = 'role'
	id = Column(Integer(), primary_key=True)
	name = Column(String(80), unique=True)
	description = Column(String(255))

	def __init__(self, name, description):
		super(Role, self).__init__()
		self.name = name
		self.description = description

class User(Base, UserMixin):

	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	email = Column(String(255), unique=True)
	username = Column(String(255))
	password_hash = Column(String(255))
	review = Column(String(255))
	roles = relationship('Role', secondary='roles_users',
backref=backref('user', lazy='dynamic'))
	tokens = Column(TEXT)
####Flask Security Modules ##############
	current_login_at = Column(String(100))
	last_login_ip = Column(String(100))
	current_login_ip = Column(String(100))
	login_count = Column(String(100))
	created_at = Column(DateTime, default=datetime.utcnow())

	

	@property
	def password(self):
		"""
		Prevent pasword from being accessed
		"""
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		"""
		Set password to a hashed password
		"""
		#pepper = os.environ.get('SECRET_SALT')
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""
		Check if hashed password matches actual password
		"""
		#pepper = os.environ.get('SECRET_SALT')
		return check_password_hash(self.password_hash, password)

	def __init__(self, username, email, password):
		super(User, self).__init__()
		self.email = email
		self.username = username
		self.password = password
	


	
	def is_authenticated(self):
		return True
 
	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False

	def get_id(self):
		
		return str(self.id)  # python 3

 
	def __repr__(self):
		return '<User %r>' % (self.username)


class Checkout(Base, UserMixin):

	__tablename__ = 'checkout'

	id = Column(Integer, primary_key=True)
	fullname = Column(String(255))
	email = Column(String(255))
	city = Column(String(255))
	state = Column(String(255))
	phone = Column(String(100))
	zipcode = Column(String(255))
	addr = Column(String(255))
	
	#adate = Column(String(255))
	#ddate = Column(String(255))
	#guests = Column(String(255))
	#nights = Column(String(255))

	room_id = Column(Integer, ForeignKey('room.id'))

	created_at = Column(DateTime, default=datetime.utcnow())

	def __init__(self, fullname="", email="", city="", state="", zipcode="", addr="", phone=""):
		super(Checkout, self).__init__()
		self.fullname = fullname
		self.email = email
		self.city = city
		self.state = state
		self.zipcode = zipcode
		self.addr = addr
		self.phone = phone

		#self.adate = adate
		#self.ddate = ddate
		#self.guests = guests
		#self.nights = nights
	

class Room(Base, UserMixin):

	__tablename__ = 'room'

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	#author = Column(String(60), nullable=False)
	description = Column(TEXT, nullable=False)
	price = Column(String(100), nullable=False)
	home_img = Column(String(100), nullable=False)
	img1_url = Column(String(100), nullable=False)
	img2_url = Column(String(100), nullable=False)
	img3_url = Column(String(100), nullable=False)
	mode = Column(String(100), nullable=False)
	capacity = Column(String(100), nullable=False)

	checkouts = relationship('Checkout', backref='room',
                                lazy='dynamic')

	added_on = Column(DateTime, default=datetime.utcnow())


	def __init__(self, title, description, price, home_img, img1_url, img2_url, img3_url, mode, capacity):
		super(Room, self).__init__()
		self.title = title
		self.description = description
		self.price = price
		self.home_img = home_img
		self.img1_url = img1_url
		self.img2_url = img2_url
		self.img3_url = img3_url
		self.mode = mode
		self.capacity = capacity
		


class Event(Base, UserMixin):

	__tablename__ = 'events'
	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	#author = Column(String(60), nullable=False)
	description = Column(TEXT, nullable=False)
	home_img = Column(String(100), nullable=False)
	tags = Column(String(100), nullable=False)
	added_on = Column(DateTime, default=datetime.utcnow())

	def __init__(self, title, description, home_img, tags):
		super(Event, self).__init__()
		self.title = title
		self.description = description
		self.home_img = home_img
		self.tags = tags


class Blog(Base, UserMixin):

	__tablename__ = 'blogs'

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	img_off = Column(String(100), nullable=False)
	#author = Column(String(60), nullable=False)
	body = Column(TEXT, nullable=False)
	tags = Column(String(100), nullable=False)
	posted_on = Column(DateTime, default=datetime.utcnow())

	def __init__(self, title, img_off, body, tags):
		super(Blog, self).__init__()
		self.title = title
		self.img_off = img_off
		#self.author = author
		self.body = body
		self.tags = tags

class Contact(Base, UserMixin):

	__tablename__ = 'contacts'

	id = Column(Integer, primary_key=True)
	name = Column(String(60), index=True)
	mail = Column(String(60), index=True)
	sub = Column(String(60), unique=True)
	msg = Column(String(500), index=True)
	msg_time = Column(DateTime, default=datetime.utcnow())

	def __init__(self, name, mail, sub, msg):
		super(Contact, self).__init__()
		self.name = name
		self.mail = mail
		self.sub = sub
		self.msg = msg