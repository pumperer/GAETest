# coding=utf-8
'''
Created on 2014. 7. 3.

@author: HyunSoo
'''
import jinja2
import os
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.api import users
from Account import Account

import webapp2


class Admin(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        if user:
            if user.email() == 'pumperer@gmail.com':
                query = Account.query()
                result = query.fetch() 
                template_values = {
                    'accounts': result,
                }
                template = jinja_env.get_template('Admin.html')
                self.response.out.write(template.render(template_values))
            else:
                self.response.out.write('WARNING!!!')
        else:
            self.redirect(users.create_login_url(self.request.uri))
        
class AddUser(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        useremail = self.request.get('email')
        newUser = Account()
        newUser.username = username
        newUser.email = useremail
        #newUser.key = ndb.Key(Account, '')
        newUser.put()
        self.redirect('/admin')

application = webapp2.WSGIApplication([('/admin', Admin), ('/adduser', AddUser)], debug=True)