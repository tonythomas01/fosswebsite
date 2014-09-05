from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from register.models import User_info
from django.db.models import Q

# Create your views here.
from register.views import logged_in


def home(request):
    """
    Landing page
    """
    if logged_in(request):
        is_loggedin = True
        username = request.session['username']
    else:
        is_loggedin = False
        username = None

    return render_to_response('home.html', \
            {'is_loggedin':is_loggedin, \
            'username':username}, \
            RequestContext(request))


def search(request):
    """
    Search view
    """
    search_field = request.GET['search_field']
    #if search field is empty
    if not search_field:
        return HttpResponseRedirect('/')

    #if search field is not empty
    else:
        result = []
        is_empty = True

        search_list = search_field.split(' ')
        for term in search_list:
            #search in the firstname and lastname of all members.
            rs_obj = User_info.objects \
                    .filter(Q(firstname__icontains=term) | \
                    Q(lastname__icontains=term))
            for result_object in rs_obj:
                if result_object not in result:
                    result.append(result_object)

        #if search result is not empty
        if result:
            is_empty = False

        return render_to_response( \
                'search_result.html', \
                {'is_empty':is_empty, \
                'is_loggedin':logged_in(request), \
                'username':request.session['username'], \
                'result':result}, \
                RequestContext(request))
