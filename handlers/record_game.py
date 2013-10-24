import jinja2
import webapp2
import os
import models
from datetime import datetime

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

class RecordGameHandler(webapp2.RequestHandler):
    def get(self):
    	factions = models.Faction.query().fetch(100)
    	results = models.Result.query().fetch(100)
    	casters = models.Warcaster.query().fetch(200)
    	template = jinja_environment.get_template('record.html')
    	self.response.out.write(template.render(factions=factions, results=results, casters=casters))

    def post(self):
    	pointLevel = self.request.get('pointLevel')
    	real_points = int(pointLevel)
    	userCaster = self.request.get('userCaster')
    	userFaction = self.request.get('userFaction')
    	opponentName = self.request.get('opponentName')
    	opponentFaction = self.request.get('opponentFaction')
    	opponentCaster = self.request.get('opponentCaster')
    	result = self.request.get('result')
    	date = self.request.get('date')
    	real_date = datetime.strptime(date,'%Y-%m-%d')
    	game = models.Game(date=real_date, 
    		player_name='test',
    		player_faction=userFaction,
    		player_warcaster=userCaster,
    		opponent_name=opponentName,
    		opponent_faction=opponentFaction,
    		opponent_warcaster=opponentCaster,
    		size=real_points,
    		result=result)
    	game.put()
    	self.redirect('/record')

app = webapp2.WSGIApplication([
    ('/record', RecordGameHandler)
], debug=True)
