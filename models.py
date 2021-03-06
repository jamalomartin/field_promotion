from google.appengine.ext import ndb
from google.appengine.api import memcache
import logging

class Game(ndb.Model):
	date = ndb.DateProperty(required=True)
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