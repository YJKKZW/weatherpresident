# coding:utf-8
import urllib2, sys
import json
import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010').read()
        resp = json.loads(resp)

        html  = u''
        html += resp['forecasts'][0]['date']
        html += u'の東京の天気は<span style="color:blue">'
        html += resp['forecasts'][0]['telop']
        html += u'</span>です'
        self.response.write(html)

class HelloWebapp2Hoge(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, Glossom Get')
    def post(self):
        self.response.write('Hello, Glossom Post')

class Weather(webapp2.RequestHandler):
    def get(self):
        citycode = '130010' #tokyo
        resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

        ## JSON自体を表示
        #self.response.headers['Content-Type'] = 'application/json'
        #self.response.out.write(resp)

        # 文字列で表示
        # 読み込んだJSONデータをディクショナリ型に変換
        self.response.headers['Content-Type'] = 'text/plain'
        resp = json.loads(resp)
        output = u"citycodeは%sです\n" % citycode
        output += "**************************\n"
        output += resp['title']
        output += "\n**************************\n"
        output += resp['description']['text']
        output += "\n"

        for forecast in resp['forecasts']:
            output += "**************************\n"
            output += forecast['dateLabel'] + '(' + forecast['date'] + ')' + "\n"
            output += forecast['telop'] + "\n"
        output += "**************************\n"
        self.response.out.write(output)

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ('/hoge', HelloWebapp2Hoge),
    ('/weather', Weather),
], debug=True)
