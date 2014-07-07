'''
Created on 2014. 7. 4.

@author: ALPO
'''

from google.appengine.ext import ndb

class DailyReportModel(ndb.Model):
    username = ndb.StringProperty()
    report = ndb.StringProperty()
    reportDay = ndb.DateProperty()
    writeTime = ndb.DateTimeProperty()
    
    def getReportDay(self):
        return self.reportDay.strftime("%Y-%m-%d")