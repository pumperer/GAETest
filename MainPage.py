# coding=utf-8
import jinja2
import os
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

import webapp2
import datetime
import urllib
import cgi
import Account

class MainPage(webapp2.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        self.response.out.write('헬로~! Hello, My World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


application = webapp2.WSGIApplication([('/', MainPage)], debug=True)