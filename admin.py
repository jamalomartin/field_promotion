import jinja2
import webapp2
import os
import logging
import models
import time

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
		elif self.request.get('caster'):
			self.add_caster()
		time.sleep(2)
		self.redirect('/admin', 'get')

	def populate_page(self):
		factions = models.Faction.query().fetch(100)
		results = models.Result.query().fetch(100)
		casters = models.Warcaster.query().fetch(200)
		
		# TODO this is a bad idea, but will work for now.  learn about KeyProperty
		for caster in casters:
			caster.factionName = caster.faction.get().name

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
		if self.request.get('victory') == 'true':
			victory_boolean = True

		result = models.Result(name=resultName, victory=victory_boolean)
		result.put()

	def add_caster(self):
		casterName = self.request.get('casterName')
		casterFaction = self.request.get('casterFaction')
		matched_faction = None
		factions = models.Faction.query().fetch(100)
		for faction in factions:
			if faction.name == casterFaction:
				matched_faction = faction
		caster = models.Warcaster(name=casterName, faction=matched_faction.key)
		caster.put()

app = webapp2.WSGIApplication([
	('/admin', AdminHandler)
], debug=True)
