from google.appengine.ext import ndb

class Faction(ndb.Model):
	name = ndb.StringProperty()
	abbrev = ndb.StringProperty()

class Warcaster(ndb.Model):
	name = ndb.StringProperty()
	faction = ndb.ReferenceProperty(Faction)

class Result(ndb.Model):
	name = ndb.StringProperty()

class Match(ndb.Model):
	date = ndb.DateProperty()
	player_name = ndb.StringProperty()
	player_faction = ndb.ReferenceProperty(Faction)
	player_warcaster = ndb.ReferenceProperty(Warcaster)
	opponent_name = ndb.StringProperty()
	opponent_faction = ndb.ReferenceProperty(Faction)
	opponent_warcaster = ndb.ReferenceProperty(Warcaster)
	size = ndb.IntegerProperty()
	result - ndb.ReferenceProperty(Result)
