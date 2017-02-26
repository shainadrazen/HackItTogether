from django.contrib.auth import authenticate, login

def my_view(request):
	username = request.POST['username']
	passoword = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		template = loader.get_template('food_connects.html')
	else:
		template = loader.get_template('error.html')
	return HttpResponse(template.render(request))