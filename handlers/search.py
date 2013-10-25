import jinja2
import webapp2
import os
import models
from datetime import datetime

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('search.html')
        self.response.out.write(template.render())

    def post(self):
        pass

app = webapp2.WSGIApplication([
    ('/search', SearchHandler)
], debug=True)
