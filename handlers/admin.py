import jinja2
import webapp2
import os
import logging
import models
import time

jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

class AdminHandler(webapp2.RequestHandler):

	def get(self):
		self.populate_page()

	def post(self):
		if self.request.get('faction'):
			self.add_faction()
		elif self.request.get('result'):
			self.add_result()
		elif self.request.get('caster'):
			self.add_caster()
		time.sleep(2)
		self.redirect('/admin', 'get')

	def populate_page(self):
		factions = models.get_factions()
		results = models.get_results()
		casters = models.get_casters()

		template = jinja_environment.get_template('admin.html')
		self.response.out.write(template.render(factions=factions, results=results, casters=casters))

	def add_faction(self):
		factionName = self.request.get('factionName')
		factionAbbrev = self.request.get('factionAbbrev')
		faction = models.Faction(name=factionName, abbrev=factionAbbrev)
		faction.put()

	def add_result(self):
		resultName = self.request.get('resultName')
		victory_boolean = False
		draw_boolean = False
		teaching_boolean = False
		
		if self.request.get('victory') == 'true':
			victory_boolean = True
		if self.request.get('draw') == 'true':
			draw_boolean = True
		if self.request.get('teaching') == 'true':
			teaching_boolean = True

		result = models.Result(name=resultName, victory=victory_boolean, draw=draw_boolean, teaching=teaching_boolean)
		result.put()

	def add_caster(self):
		casterName = self.request.get('casterName')
		casterFaction = self.request.get('casterFaction')
		caster = models.Warcaster(name=casterName, faction_name=casterFaction)
		caster.put()

app = webapp2.WSGIApplication([
	('/admin', AdminHandler)
], debug=True)
