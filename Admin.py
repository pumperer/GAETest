# coding=utf-8
'''
Created on 2014. 7. 3.

@author: HyunSoo
'''
import jinja2
import os
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.ext import ndb
from Account import Account

import webapp2


class Admin(webapp2.RequestHandler):
    def get(self):
        query = Account.query()
        result = query.fetch() 
        template_values = {
            'accounts': result,
        }
        template = jinja_env.get_template('Admin.html')
        self.response.out.write(template.render(template_values))
        
class AddUser(webapp2.RequestHandler):
    def post(self):
        newUser = Account()
        newUser.username = self.request.get('username')
        newUser.email = self.request.get('email')
        newUser.key = ndb.Key('Account', newUser.username)
        newUser_key = newUser.put()
        self.redirect('/admin')

application = webapp2.WSGIApplication([('/admin', Admin), ('/adduser', AddUser)], debug=True)