'''
Created on 2014. 7. 4.

@author: ALPO
'''

from google.appengine.ext import ndb
#import datetime

class DailyReportModel(ndb.Model):
    username = ndb.StringProperty()
    report = ndb.StringProperty()
    reportDay = ndb.DateProperty()
    
    def getReportDay(self):
        return str(self.reportDay.year) + '-' + str(self.reportDay.month) + '-' + str(self.reportDay.day)
    
# class DailyReport():
#     username = 'EMPTY'
#     report = 'EMPTY'
#     reportDay = datetime.date.today()
#     
#     def getReportDay(self):
#         return self.reportDay.year + '.' + self.reportDay.month + '.' + self.reportDay.day