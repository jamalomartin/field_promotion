import webapp2
from django.shortcuts import render_to_response

class MainHandler(webapp2.RequestHandler):
    def get(self):
        return render_to_response('templates/app.html')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
