'''
Created on 2014. 7. 4.

@author: ALPO
'''

import jinja2
import os
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.api import users
from DailyReport import DailyReportModel

import webapp2
import datetime
from collections import OrderedDict

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            
            #current user name
            current_username = user.nickname()
            
            #report query
            reportQry = DailyReportModel.query().order(-DailyReportModel.reportDay, -DailyReportModel.writeTime)
            reportFetch = reportQry.fetch()
            
            reportDict = OrderedDict()
            for item in reportFetch:
                reportDay = item.getReportDay()
                if reportDict.has_key(reportDay):
                    reportDict[reportDay].append(item)
                else:
                    reportDict[reportDay] = [item]
                    
            # sort
            OrderedDict(sorted(reportDict.items(), key=lambda t: t[0], reverse=True))
            
            # jinja2 param
            template_values = {
                'current_username' : current_username,
                'report_dict' : reportDict,
                'date_today' : datetime.datetime.now().strftime("%Y-%m-%d")
            }
            template = jinja_env.get_template('MainPage.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

class AddDailyReport(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        contents = self.request.get('contents')
        lines = contents.splitlines()
        toDB = ''
        for line in lines:
            toDB += line
            toDB += '<br/>'
        reportday = self.request.get('writedatetime')
        reportModel = DailyReportModel()
        reportModel.username = username
        reportModel.report = toDB
        reportModel.reportDay = datetime.datetime.strptime(reportday, "%Y-%m-%d").date()
        reportModel.writeTime = datetime.datetime.now()
        reportModel.put()
        self.redirect('/')

application = webapp2.WSGIApplication([('/', MainPage), ('/addreport', AddDailyReport)], debug=True)