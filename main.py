# coding:utf-8
import urllib2, sys
import json
import webapp2
import os

import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
        resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010').read()
        resp = json.loads(resp)

        template = JINJA_ENVIRONMENT.get_template("index.html")
        template_vars = {
        "area":resp['title'],
        "forecasts":resp['forecasts'],
        "descriptiondetail":resp['description']['text'],
        }
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
