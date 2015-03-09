from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from account.models import User, UserRegisterForm, UserLoginForm
from django.contrib import auth

# Create your views here.

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/share')
	if request.method == 'POST': 
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			if not User.objects.filter(email=email):
				user=User.objects.create_user(username,email,password)  
				user.is_active=True  
				user.save()
				return HttpResponseRedirect('/account/login')
	else:
		form = UserRegisterForm()
	return render(request, 'register.html', {'form': form})

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/share')
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect( '/share' )
	else:
		form = UserLoginForm()
	return render(request, 'login.html', {'form': form})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect( '/' )

def showaccount(request, id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/login')
	if request.user.id == id:
		showself(request)
	else:
		user = User.objects.get(id=id)
		return render(request, 'showaccount.html', {'currentuser':request.user,'user':user})

def showself(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/login')
	else :
		return render(request, 'showself.html', {'currentuser':request.user,'user':request.user})