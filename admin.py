import jinja2
import webapp2
import os
import logging
import models

jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class AdminHandler(webapp2.RequestHandler):
	def get(self):
		factions = models.Faction.query().fetch(100)
		template = jinja_environment.get_template('admin.html')
		self.response.out.write(template.render(factions=factions))

	def post(self):
		factionName = self.request.get('factionName')
		factionAbbrev = self.request.get('factionAbbrev')
		faction = models.Faction(name=factionName, abbrev=factionAbbrev)
		faction.put()
		factions = models.Faction.query().fetch(100)
		factions.append(faction)
		template = jinja_environment.get_template('admin.html')
		self.response.out.write(template.render(factions=factions))

app = webapp2.WSGIApplication([
	('/admin', AdminHandler)
], debug=True)
