'''
Created on 2014. 7. 3.

@author: HyunSoo
'''

from google.appengine.ext import ndb

class Account(ndb.Model):
    username = ndb.StringProperty()
    email = ndb.StringProperty()