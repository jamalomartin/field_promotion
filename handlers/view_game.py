import jinja2
import webapp2
import os
import models
from google.appengine.api import namespace_manager
from google.appengine.api import users
from datetime import datetime

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

class ViewHandler(webapp2.RequestHandler):
    def get(self):
    	namespace_manager.set_namespace(users.get_current_user().user_id())
    	games = models.Game.query().order(-models.Game.date).fetch(1000)
        template = jinja_environment.get_template('view_game.html')
        self.response.out.write(template.render(games=games))

app = webapp2.WSGIApplication([
    ('/view', ViewHandler)
], debug=True)
