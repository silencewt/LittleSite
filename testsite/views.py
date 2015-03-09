from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def welcome(request):
	if request.user.is_authenticated():
		return  HttpResponseRedirect('/share')
	else :
		return  HttpResponseRedirect('/account/login')

import urllib, urllib2
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def google(request):
	if request.method == 'POST':
		data = urllib.urlencode({'wd':request.POST['sinput']})
		req = urllib2.Request('http://www.baidu.com/s?'+data)
		req.add_header('User-Agent', 'Chrome')
		res = urllib2.urlopen(req)
		html = res.read()
		response = HttpResponse()
		response.write(html)
		return response
	return render(request, 'google.html')