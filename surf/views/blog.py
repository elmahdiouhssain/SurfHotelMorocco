# -*- coding: utf-8 -*-
from flask import Blueprint, abort, flash, g, jsonify, redirect, \
	render_template, request, url_for

from surf.form import ContactForm, GetRoom, RegistrationForm, AddRoom, Addpost, Moreevent, Available
from surf.database import User, RolesUsers, Role, User, Room, Event, Blog, Contact, Checkout, db_session, init_db
from sqlalchemy.orm import subqueryload
from sqlalchemy import desc


blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.route('/post/<id_slug:blog_id>')
def post(blog_id):


	#blogs = Blog.query.order_by(desc(Blog.id)).limit(2)
	blogs = Blog.query.filter_by(id=blog_id).one()

	url_for('blog.post', blog_id=blogs)


	return render_template('/blogindex.html', blogs=blogs, title='Blog')