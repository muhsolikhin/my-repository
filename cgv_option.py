import requests
import json
import datetime
import time




fheader = {'Host': 'app.cgv.id'}

r = requests.get('https://app.cgv.id/api/locations', headers = fheader)

fjson = json.loads(r.text)

data = fjson['data']

number = 1
for location in data:
	print (number, location['name'])
	number +=1

#is_available = fjson['data']['rows'][0]['seats'][2]['is_available']
#print (fjson)

