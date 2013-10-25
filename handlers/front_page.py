import jinja2
import webapp2
import os
import models
import logging
from datetime import datetime
from google.appengine.api import users

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

class FrontHandler(webapp2.RequestHandler):
    def get(self):
    	admin = users.is_current_user_admin()
        template = jinja_environment.get_template('front_page.html')
        self.response.out.write(template.render(admin=admin))

    def post(self):
        direction = self.request.get('direction')
    	self.redirect('/'+direction.lower())

app = webapp2.WSGIApplication([
    ('/', FrontHandler)
], debug=True)
