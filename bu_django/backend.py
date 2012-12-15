from django.core.mail import EmailMessage
from django.template.loader import render_to_string
#from django.cron import CronJobBase, Schedule
import urllib2
import json
import logging
from bu_django.local_settings import *

def send_testmail(subject, content, icon):
	#email = EmailMessage('Bring umbrella!', 'It is going to rain today:)\n\nSent by me', to=['linuxcity.jn@gmail.com'])
	email_content = render_to_string('email.html', {'icon': icon, 'content' : content})
	#email = EmailMessage(subject, email_content, to=['linuxcity.jn@gmail.com'])
	email = EmailMessage(subject, email_content, to=['linuxcity.jn@gmail.com'], bcc=MAILLING_LIST)
	email.content_subtype = 'html'
	logging.info('sending test mail!')
	return email.send()

def send_mail():
    return
    
# class CheckWeatherCron(CronJobBase):
# 	RUN_AT_TIMES = ['05:00']
# 	schedule = Schedule(run_at_times=RUN_AT_TIMES)
# 	code = 'check_weather'

# 	def do(self):
# 		url = 'http://api.wunderground.com/api/4fd7dd818e23db7f/forecast/q/57.659056,11.918264.json'
# 		response = urllib2.urlopen(url)
# 		raw_data = response.read()

# 		with open('weather.log', 'w') as f:
# 			f.write(raw_data)

# 		data = json.loads(raw_data)
# 		forecast = data[u'forecast'][u'simpleforecast'][u'forecastday'][0][u'conditions']

# 		if 'Rain' in forecast:
# 			print("It's gonna rain!")
# 			send_testmail()
