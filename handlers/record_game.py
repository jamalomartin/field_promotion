import jinja2
import webapp2
import os
import models
from google.appengine.api import namespace_manager
from google.appengine.api import users
from datetime import datetime
import data_utils

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

class RecordGameHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('record.html')
    	self.response.out.write(template.render())

    def post(self):
        namespace_manager.set_namespace(users.get_current_user().user_id())
        import logging
        logging.warn(users.get_current_user().user_id())
    	pointLevel = self.request.get('pointLevel')
    	real_points = int(pointLevel)
    	userCaster = self.request.get('userCaster')
    	userFaction = self.request.get('userFaction')
    	opponentName = self.request.get('opponentName')
    	opponentFaction = self.request.get('opponentFaction')
    	opponentCaster = self.request.get('opponentCaster')
    	date = self.request.get('date')
    	real_date = datetime.strptime(date,'%Y-%m-%d')
        result = self.request.get('result')
    	result_types = self.get_game_results_from_result_name(result)
        game = models.Game(date=real_date, 
    		player_faction=userFaction,
    		player_warcaster=userCaster,
    		opponent_name=opponentName,
    		opponent_faction=opponentFaction,
    		opponent_warcaster=opponentCaster,
    		size=real_points,
    		result=result,
            won=result_types[0],
            draw=result_types[1],
            teaching=result_types[2])
    	game.put()
    	self.redirect('/record')

    def get_game_results_from_result_name(self, result_name):
        results = data_utils.get_all_results()
        for result in results:
            if result.get('name') == result_name:
                return result.get('won'), result.get('draw'), result.get('teaching')

app = webapp2.WSGIApplication([
    ('/record', RecordGameHandler)
], debug=True)
