from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.shortcuts import render
from mysite.models import *
from django.core.mail import EmailMessage


def index(request):
	print("another deubug")
	return render(request, 'index.html')

@csrf_protect
def food(request):
	print(request.POST.get('address'))
	address = request.POST.get('address')
	emailBody = 'Food is ready for pickup at ' + address
	email = EmailMessage('Food Alert', emailBody, to=['shainadrazen@gmail.com'])
	email.send()
	return render(request, 'thankyou.html')