# Create your views here.
from django	import forms
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

class EmailForm(forms.Form):
	email = forms.EmailField()

def form(request):
	errors = []
	if request.method == 'GET':
		form = EmailForm
		params = {
			'form': form
		}
		return render_to_response('signup.html', params, context_instance = RequestContext(request))
	elif request.method == 'POST':
		if not errors:
			return HttpResponse('Accepted!')