from google.appengine.ext import ndb

class Faction(ndb.Model):
	name = ndb.StringProperty()
	abbrev = ndb.StringProperty()

class Warcaster(ndb.Model):
	name = ndb.StringProperty()
	faction = ndb.KeyProperty(kind=Faction)

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
