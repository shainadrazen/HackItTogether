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