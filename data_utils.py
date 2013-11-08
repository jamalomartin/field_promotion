import json

def get_all_results():
	result_data = json.loads(file('results.json').read())
	return result_data