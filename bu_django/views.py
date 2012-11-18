import datetime

from django	import forms
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from backend import send_testmail

class EmailForm(forms.Form):
	email = forms.EmailField()

def home(request):
	now = datetime.datetime.now()
	form = EmailForm
	params = {
		'current_date':now,
		'form': form
	}
	return render_to_response('beta.html', params)

def mail_content(request):
	params = {
		'content': 'Clear in the morning, then overcast with a chance of rain. High of 13C. Windy. Winds from the West at 25 to 35 km/h. Chance of rain 30%.',
		'icon'   : 'http://icons-ak.wxug.com/i/c/k/chancerain.gif'
	}
	return render_to_response('email.html', params)