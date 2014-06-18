from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from register.models import User_info
from django.db.models import Q
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

def search(request):
	search_field = request.GET['search_field']
	if not search_field:
		return HttpResponseRedirect('/')
	else:
		result = []
		person=[]
		is_empty = True
		search_list = search_field.split(' ')
		for term in search_list:
			#return HttpResponse(term)
			rs_obj = User_info.objects.filter(Q(firstname__icontains=term)|Q(lastname__icontains=term))
			for result_object in rs_obj:
				if result_object not in result:
					result.append(result_object)
					person.append(result_object.firstname + " " + result_object.lastname)
		if result:
			is_empty = False
		return render_to_response('search_result.html',{'is_empty':is_empty, 'person':person},RequestContext(request))
'''
def info_page(request):
	is_loggedin = False
	information = False
	user_name = ''
	if 'is_loggedin' in request.session and request.session['is_loggedin']:
		is_loggedin = True
		user_name = request.session['username']
	return render_to_response('info.html',{'is_loggedin':is_loggedin, 'username':user_name ,'information':information},RequestContext(request))

def info_det(request,info_type):
        is_loggedin = False
	information = True
	user_name = ''
        if 'is_loggedin' in request.session and request.session['is_loggedin']:
                is_loggedin = True
		user_name=request.session['username']
	return render_to_response('info.html',{'is_loggedin':is_loggedin,'username':user_name, 'information':information, 'info_type':info_type},RequestContext(request))
'''

