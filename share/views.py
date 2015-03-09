from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from share.models import Share
from account.models import User
import json

# Create your views here.
def show(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/login')
	else :
		typelist = [i[0] for i in Share.TYPE_CHOICES]
		sharelist = Share.objects.all()
		for i in sharelist:
			if len(i.content)>=50:
				i.content = repr(i.content[:48])+'...'
		request.session['next'] = len(sharelist)
		return render(request, 'share.html', { 'currentuser':request.user,'typelist':typelist,'sharelist':sharelist })

'''def create(request):
	response = HttpResponse()
	response['Content-Type'] = 'text/javascript'
	if request.is_ajax() and request.method == 'POST':
		name = request.POST['name']
		content = request.POST['content']
		type = request.POST['type']
		shareitem = Share(name=name, content=content, type=type, author=request.user)
		shareitem.save()
		t = { 'status':'success' }
	else :
		print 'failed'
		t = { 'status':'error' }
	response.write( json.dumps(t) )
	return response
'''

def create(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/login')
	if request.method == 'POST':
		name = request.POST['name']
		content = request.POST['content']
		type = 'text'
		shareitem = Share(name=name, content=content, type=type, author=request.user)
		shareitem.save()
		return HttpResponseRedirect('/share')
	return render(request, 'create.html',{'currentuser':request.user})

def showtext(request, id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/login')
	text = Share.objects.get(id=id)
	return render(request, 'showtext.html', {'currentuser':request.user,'text':text})