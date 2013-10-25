from google.appengine.ext import ndb
from google.appengine.api import memcache
import logging

class Faction(ndb.Model):
	name = ndb.StringProperty()
	abbrev = ndb.StringProperty()

class Warcaster(ndb.Model):
	name = ndb.StringProperty(required=True)
	faction_name = ndb.StringProperty()

class Result(ndb.Model):
	name = ndb.StringProperty()
	victory = ndb.BooleanProperty()
	draw = ndb.BooleanProperty()
	teaching = ndb.BooleanProperty()

class Game(ndb.Model):
	date = ndb.DateProperty(required=True)
	player_name = ndb.StringProperty(required=True)
	player_faction = ndb.StringProperty(required=True)
	player_warcaster = ndb.StringProperty(required=True)
	opponent_name = ndb.StringProperty()
	opponent_faction = ndb.StringProperty(required=True)
	opponent_warcaster = ndb.StringProperty(required=True)
	size = ndb.IntegerProperty()
	result = ndb.StringProperty(required=True)
	won = ndb.BooleanProperty()
	draw = ndb.BooleanProperty()
	teaching = ndb.BooleanProperty()

def get_casters():
	casters = memcache.get('caster_list')
	if not casters:
		casters = Warcaster.query().order(Warcaster.name).fetch(200)
		if not memcache.add('caster_list', casters):
			logging.error('Memcache caster set failed.')
	return casters

def get_factions():
	factions = memcache.get('faction_list')
	if not factions:
		factions = Faction.query().order(Faction.name).fetch(100)
		if not memcache.add('faction_list', factions):
			logging.error('Memcache faction set failed.')
	return factions

def get_results():
	results = memcache.get('result_list')
	if not results:
		results = Result.query().order(Result.name).fetch(100)
		if not memcache.add('result_list', results):
			logging.error('Memcache result set failed.')
	return results