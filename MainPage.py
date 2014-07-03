# coding=utf-8
import jinja2
import os
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.ext import ndb
from google.appengine.api import users
from Account import Account

import webapp2
import datetime
import urllib
import cgi

class MainPage(webapp2.RequestHandler):
    
    
    def get(self):
        template = jinja_env.get_template('MainPage.html')
        self.response.out.write(template.render(''))


application = webapp2.WSGIApplication([('/', MainPage)], debug=True)