#! /usr/bin/python3.6

import logging
import sys

activate_this = '/var/www/webapp/vnv3/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/webapp/')
from app import app as application
application.secret_key = 'qsdhqsidhqhsdhqsjdjkqhsdjqshdjkqshkqj'