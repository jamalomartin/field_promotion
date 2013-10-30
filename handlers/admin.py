import jinja2
import webapp2
import os
import logging
import models
import time
import json
import data_utils

jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

class AdminHandler(webapp2.RequestHandler):

	def get(self):
		self.populate_page()

	def post(self):
		if self.request.get('result'):
			self.add_result()

		time.sleep(2)
		self.redirect('/admin', 'get')

	def populate_page(self):
		casters = data_utils.get_all_casters()
		factions = data_utils.get_all_factions()
		results = data_utils.get_all_results()

		template = jinja_environment.get_template('admin.html')
		self.response.out.write(template.render(factions=factions, results=results, casters=casters))

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

app = webapp2.WSGIApplication([
	('/admin', AdminHandler)
], debug=True)
