import jinja2
import webapp2
import os
import logging
import models

jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class AdminHandler(webapp2.RequestHandler):

	def get(self):
		self.populate_page()

	def post(self):
		if self.request.get('faction'):
			self.add_faction()
		elif self.request.get('result'):
			self.add_result()

	def populate_page(self, factions=None, results=None):
		if not factions:
			factions = models.Faction.query().fetch(100)
		if not results:
			results = models.Result.query().fetch(100)
		template = jinja_environment.get_template('admin.html')
		self.response.out.write(template.render(factions=factions, results=results))

	def add_faction(self):
		factionName = self.request.get('factionName')
		factionAbbrev = self.request.get('factionAbbrev')
		faction = models.Faction(name=factionName, abbrev=factionAbbrev)
		faction.put()
		factions = models.Faction.query().fetch(100)
		factions.append(faction)
		self.populate_page(factions=factions)

	def add_result(self):
		resultName = self.request.get('resultName')
		victory_boolean = False
		if self.request.get('victory') == 'true':
			victory_boolean = True

		result = models.Result(name=resultName, victory=victory_boolean)
		result.put()
		results = models.Result.query().fetch(100)
		results.append(result)
		self.populate_page(results=results)

app = webapp2.WSGIApplication([
	('/admin', AdminHandler)
], debug=True)
