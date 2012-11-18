from django.core.management.base import BaseCommand, CommandError
from bu_django.backend import send_testmail
import urllib2
import json

class Command(BaseCommand):
	help = 'Check weather'

	def handle(self, *args, **options):
		url = 'http://api.wunderground.com/api/4fd7dd818e23db7f/forecast/q/57.659056,11.918264.json'
		response = urllib2.urlopen(url)
		raw_data = response.read()
		with open('weather.log', 'w') as f:
			f.write(raw_data)

		data = json.loads(raw_data)
		forecast = data[u'forecast'][u'simpleforecast'][u'forecastday'][0][u'conditions']
		forecast_content = data[u'forecast'][u'txt_forecast'][u'forecastday'][0][u'fcttext_metric']
		forecast_icon    = data[u'forecast'][u'txt_forecast'][u'forecastday'][0][u'icon_url']
		if 'Rain' in forecast:
			print("It's gonna rain!")
			send_testmail( subject = 'Bring umbrealla!', icon = forecast_icon, content = forecast_content )
		elif 'Thunderstorm' in forecast:
			print("We will have thunderstorm!")
			send_testmail( subject = 'Bring umbrealla!', content = forecast_content )

		#self.stdout.write('data:\n')
		#self.stdout.write(data['forecast']) 