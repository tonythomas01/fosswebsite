from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def home(request):
	is_loggedin = False
	username = ''
	if 'is_loggedin' in request.session:
		if request.session['is_loggedin']:
			is_loggedin = True
			username = request.session['username']
	return render_to_response('home.html',{'is_loggedin':is_loggedin, 'username':username},RequestContext(request))

def homeredirect(request):
	return HttpResponseRedirect('/home')
