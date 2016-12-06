import json

def write_to_json(data):
  with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=2, sort_keys=False, separators=(',',':'))

def open_json(file_name):
  with open(file_name) as data_file:
    data = json.load(data_file)
    return data
