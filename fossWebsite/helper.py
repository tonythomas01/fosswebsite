# Django libraries
from django.shortcuts import render_to_response


def error_key(request):
    """
    Key error response
    """
    return render_to_response('keyerror.html', \
            {'reason':'Key Error'}, \
            RequestContext(request))


def csrf_failure(request, reason=""):
    """
    CSRF failure response
    """
    return render_to_response('keyerror.html', \
            {'reason':reason}, \
            RequestContext(request))


def logged_in(request):
    """
    To check if the user is logged in or not 
    """
    try:
        if request.session['is_loggedin']:
            return True
        else:
            return False
    except KeyError:
        return False


