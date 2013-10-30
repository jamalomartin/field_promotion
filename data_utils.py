import json

def get_all_casters():
	caster_data = json.loads(file('casters.json').read())
	casters = []
	for faction in caster_data:
		for person in caster_data[faction]:
			casters.append(person)
	casters.sort()
	return casters

def get_all_factions():
	faction_data = json.loads(file('casters.json').read())
	factions = []
	for faction in faction_data:
		factions.append(faction)
	factions.sort()
	return factions

def get_all_results():
	result_data = json.loads(file('results.json').read())
	return result_data