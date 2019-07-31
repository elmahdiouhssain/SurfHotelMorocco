from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, SelectField, TextAreaField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from surf.database import User, RolesUsers, Role, User, Room, Event, Blog, Checkout, Contact, db_session, init_db

class LoginForm(FlaskForm):


	email = StringField('Email', validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired(), validators.Length(min=4, max=8)])
	
	remember = BooleanField("Remember Me", default=False)

	#recaptcha = RecaptchaField()

	submit = SubmitField()


class RegistrationForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])

	username = StringField('Username', validators=[DataRequired()])

	password = PasswordField('Password', validators=[
										DataRequired(),
										validators.Length(min=4, max=8),
										EqualTo('confirm_password')
										])

	confirm_password = PasswordField('Confirm Password')

	recaptcha = RecaptchaField()

	submit = SubmitField('Register')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email.')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')


class ContactForm(FlaskForm):

	full_name = StringField('Full Name', validators=[DataRequired()])

	mail = StringField('Email Address', validators=[DataRequired(), Email()])

	sub = StringField('Subject', validators=[DataRequired()])

	msg = TextAreaField('Message', validators=[DataRequired()])

	recaptcha = RecaptchaField()

	submit = SubmitField('Send')


class AddRoom(FlaskForm):

	title = StringField('Title', validators=[DataRequired()])

	description = TextAreaField('Description', validators=[DataRequired()])

	price = StringField('Price $', validators=[DataRequired()])

	mode = SelectField('Status', choices=[('OPENED', 'OPENED'), ('CLOSED', 'CLOSED')])

	home_img = StringField('Official Image', validators=[DataRequired()])

	img1_url = StringField('Image 1', validators=[DataRequired()])

	img2_url = StringField('Image 2', validators=[DataRequired()])

	img3_url = StringField('Image 3', validators=[DataRequired()])

	submit = SubmitField('Send')


def validate_title(self, title):
		room = Room.query.filter_by(title=title.data).first()
		if room is not None:
			raise ValidationError('This Room is already existe.')


class Addpost(FlaskForm):

	title = StringField('Title', validators=[DataRequired()])

	body = TextAreaField('Description', validators=[DataRequired()])

	tags = StringField('Tags', validators=[DataRequired()])

	img_off = StringField('Official Image', validators=[DataRequired()])

	submit = SubmitField('Send')


def validate_title(self, title):
		post = Blog.query.filter_by(title=title.data).first()
		if post is not None:
			raise ValidationError('This Post is already existe.')

class Moreevent(FlaskForm):

	title = StringField('Title', validators=[DataRequired()])

	description = TextAreaField('Description', validators=[DataRequired()])

	tags = StringField('Tags', validators=[DataRequired()])

	home_img = StringField('Official Image', validators=[DataRequired()])

	submit = SubmitField('Save')


def validate_title(self, title):
		event = Event.query.filter_by(title=title.data).first()
		if event is not None:
			raise ValidationError('This Event is already existe.')

class GetRoom(FlaskForm):

	fullname = StringField('Full Name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	city = StringField('City', validators=[DataRequired()])
	state = StringField('State', validators=[DataRequired()])
	zipcode = StringField('Zip Code', validators=[DataRequired()])
	phone = StringField('Phone', validators=[DataRequired()])
	addr = TextAreaField('Address', validators=[DataRequired()])

	recaptcha = RecaptchaField()
	
	submit = SubmitField()

class Available(FlaskForm):

	adate = DateField()
	ddate = DateField()

	guests = SelectField(choices=[('1Guest', '1Guest'), ('2Guest', '2Guest'), ('3Guest', '3Guest'), ('4Guest', '4Guest'), ('5Guest', '5Guest')])
	nights = SelectField(choices=[('2Nights', '2Nights'), ('3Nights', '3Nights'), ('4Nights', '4Nights'), ('5Nights', '5Nights'), ('10Nights', '10Nights')])

	submit = SubmitField()