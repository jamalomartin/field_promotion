import jinja2
import webapp2
import os

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class RecordGameHandler(webapp2.RequestHandler):
    def get(self):
	  	template = jinja_environment.get_template('record.html')
	  	self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/record', RecordGameHandler)
], debug=True)
