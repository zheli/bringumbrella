from django.core.management.base import BaseCommand, CommandError
from bu_django.backend import send_testmail
from bu_django.libs.weather import weather
from bu_django.local_settings import *
import urllib2
import json

class Command(BaseCommand):
	help = 'Check weather'

	def handle(self, *args, **options):
            client = weather.Client(key = WEATHERUNDERGROUND_API_KEY)
            LOCATION = '57.659056,11.918264'
            hourly = client.request(features=['hourly'], location = LOCATION )
            forecast = client.request(features=['forecast'], location = LOCATION)
            forecast_content_day = forecast[u'forecast'][u'txt_forecast'][u'forecastday'][0][u'fcttext_metric']
            forecast_icon = forecast[u'forecast'][u'txt_forecast'][u'forecastday'][0][u'icon_url']
            forecast_today_day = forecast['forecast']['simpleforecast']['forecastday'][0]
            forecast_today_night = forecast['forecast']['simpleforecast']['forecastday'][1]
            forecast_today_day_condition = forecast_today_day[u'conditions']
            weekday = forecast_today_day[u'date'][u'weekday']
            day_lowest_temperature = int(forecast_today_day[u'low'][u'celsius'])
            night_lowest_temperature = int(forecast_today_night[u'low'][u'celsius'])
            average_wind_speed = int(forecast_today_day[u'avewind'][u'kph'])
            subject = ''

            #save the logs
            with open('forecast.log', 'w') as f:
                f.write(json.dumps(forecast))

            with open('hourly.log', 'w') as f:
                f.write(json.dumps(hourly))
                
            #check the temperature
            if day_lowest_temperature < -10 or night_lowest_temperature < -10:
                if day_lowest_temperature < night_lowest_temperature:
                    lowest_temperature = day_lowest_temperature
                else:
                    lowest_temperature = night_lowest_temperature

                subject = u'Cold(%d\u00B0C). ' % lowest_temperature

            if 'Rain' in forecast_today_day_condition:
                subject = subject + 'Rainy. '

            #check the wind speed
            if subject:
                if average_wind_speed>22 and average_wind_speed<30:
                    subject = subject + 'Also windy. '

            if average_wind_speed>=30:
                subject = subject + 'Strong wind. '


            #send out the mail
            if subject:
                subject = '[%s]' % weekday + subject
                send_testmail( subject = subject, icon = forecast_icon, content = forecast_content_day )

            #data = json.loads(raw_data)
            #forecast = data[u'forecast'][u'simpleforecast'][u'forecastday'][0][u'conditions']
            #forecast_content = data[u'forecast'][u'txt_forecast'][u'forecastday'][0][u'fcttext_metric']
            #forecast_icon    = data[u'forecast'][u'txt_forecast'][u'forecastday'][0][u'icon_url']
            #if 'Rain' in forecast:
            #        print("It's gonna rain!")
            #        send_testmail( subject = 'Bring umbrealla!', icon = forecast_icon, content = forecast_content )
            #elif 'Thunderstorm' in forecast:
            #        print("We will have thunderstorm!")
            #        send_testmail( subject = 'Bring umbrealla!', content = forecast_content )

            #self.stdout.write('data:\n')
            #self.stdout.write(data['forecast'])
