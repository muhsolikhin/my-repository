import requests
import json
import datetime
import time




fheader = {'Host': 'app.cgv.id'}

r = requests.get('https://app.cgv.id/api/movie-schedules/2398525/seats', headers = fheader)

fjson = json.loads(r.text)

is_available = fjson['data']['rows'][0]['seats'][1]['is_available']

while True:

	if not is_available:
		print (datetime.datetime.now(), ' --> tidak ada')

		r = requests.get('https://app.cgv.id/api/movie-schedules/2398525/seats', headers = fheader)

		fjson = json.loads(r.text)

		is_available = fjson['data']['rows'][0]['seats'][1]['is_available']

		#time.sleep(5)

	else:
		print (datetime.datetime.now(), ' --> ada')
		#break

		r = requests.get('https://app.cgv.id/api/movie-schedules/2398525/seats', headers = fheader)

		fjson = json.loads(r.text)

		is_available = fjson['data']['rows'][0]['seats'][1]['is_available']

		#time.sleep(5)