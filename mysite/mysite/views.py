from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.shortcuts import render



def index(request):
	print("another deubug")
	return render(request, 'index.html')

@csrf_protect
def my_view(request):
	print(request.POST.get('username'))
	print(request.POST.get('password'))
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		template = 'food_connects.html'
	else:
		template = 'error.html'
	return render(request, template)

