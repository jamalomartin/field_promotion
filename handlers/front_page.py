import jinja2
import webapp2
import os
import models
import logging
from datetime import datetime

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

class FrontHandler(webapp2.RequestHandler):
    def get(self):
        logging.warn(str(self.request.headers['User-Agent']))
        template = jinja_environment.get_template('front_page.html')
        self.response.out.write(template.render())

    def post(self):
        direction = self.request.get('direction')
    	if direction == 'View':
            self.redirect('/view')
        elif direction == 'Record':
            self.redirect('/record')
        elif direction == 'Admin':
            self.redirect('/admin')
        elif direction == 'Search':
            self.redirect('/search')

app = webapp2.WSGIApplication([
    ('/', FrontHandler)
], debug=True)
