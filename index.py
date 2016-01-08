import json

# Create a dictionary (a key-value-pair structure in Python)
my_dict = {
  'Name':      'KAIRA',
  'Location':  u'Kilpisj\u00E4rvi',
  'Longitude': 20.76,
  'Latitude':  69.07
}


def write_to_json(file_name, data):
   """Final output for generated data as JSON"""

    output_file = open(file_name + '.json', "w")
    json.dump(data, output_file, indent=4)
    output_file.close()
    write_to_json('gg', data)
