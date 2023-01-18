import json

def load_data():
	with open("candidates.json", mode='r', encoding='utf-8') as file:
		data = json.load(file)
	return data
