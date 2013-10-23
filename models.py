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

class Match(ndb.Model):
	date = ndb.DateProperty()
	player_name = ndb.StringProperty()
	player_faction = ndb.KeyProperty(kind=Faction)
	player_warcaster = ndb.KeyProperty(kind=Warcaster)
	opponent_name = ndb.StringProperty()
	opponent_faction = ndb.KeyProperty(kind=Faction)
	opponent_warcaster = ndb.KeyProperty(kind=Warcaster)
	size = ndb.IntegerProperty()
	result = ndb.KeyProperty(kind=Result)
