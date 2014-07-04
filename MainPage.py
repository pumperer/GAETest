# coding=utf-8
import jinja2
import os
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.api import users
from DailyReport import DailyReportModel

import webapp2
import datetime

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            
            #current user name
            current_username = user.nickname()
            
            #report query
            reportQry = DailyReportModel.query().order(-DailyReportModel.reportDay)
            reportFetch = reportQry.fetch()
            reportDict = {}
            #onedayList = []
            for item in reportFetch:
                reportDay = item.getReportDay()
#                reportDict[reportDay].append(item)
                if reportDict.has_key(reportDay):
                    reportDict[reportDay].append(item)
                else:
                    reportDict[reportDay] = [item]

            template_values = {
                'current_username' : current_username,
                'report_dict' : reportDict,
            }
            template = jinja_env.get_template('MainPage.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

class AddDailyReport(webapp2.RequestHandler):
    def post(self):
        username = self.request.get('username')
        contents = self.request.get('contents')
        reportModel = DailyReportModel()
        reportModel.username = username
        reportModel.report = contents
        reportModel.reportDay = datetime.date.today()
        #reportModel.key = ndb.Key('DailyReport', '')
        reportModel.put()
        self.redirect('/')

application = webapp2.WSGIApplication([('/', MainPage), ('/addreport', AddDailyReport)], debug=True)