from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from register.forms import LoginForm, NewRegisterForm
from django.contrib.auth.hashers import *
from images.models import ProfileImage
from django.views.csrf import csrf_failure
from django.utils import simplejson
from django.http import Http404
from hashlib import sha512 as hash_func

def logged_in(request):
    """
    To check if the user is logged in 
    """
    try:
        if request.session['loggedinside']:
            return True
        else:
            return False
    except KeyError:
        return False


# Create your views here.
def login(request):
        error = []
        if request.method=='POST':
                request.session.set_test_cookie()
                if request.session.test_cookie_worked():
                        request.session.delete_test_cookie()
                else:
                        return HttpResponse("Please enable cookies and try again")
                form = LoginForm(request.POST)
                if form.is_valid():
                        inp_username=request.POST['username']
                        inp_password=request.POST['password']
                        user_tuple = User_info.objects.all().filter(username = inp_username)
                        if user_tuple:
                                actual_pwd = user_tuple[0].password
                                if check_password(inp_password,actual_pwd):
                                        request.session['is_loggedin'] = True
                                        request.session['username'] = inp_username
                                        return HttpResponseRedirect('/home')
                        else:
                                error.append('username not found or username password not matched')
                else:
                        error.append('incomplete form')
        else:
		if 'is_loggedin' in request.session and request.session['is_loggedin']:
			return HttpResponseRedirect('/')
		else:
                	form=LoginForm()
	return render_to_response('register/login.html',{'form':form,'error':error},RequestContext(request))


def logout(request):
        try:
                del request.session['is_loggedin']
                del request.session['username']
                request.session.flush()
        except KeyError:
                pass
        return render_to_response('register/logout.html')


def newregister(request):
    """
    Make a new registration, inserting into User_info and ProfileImage models.
    """
    if request.method == 'POST':
        request.session.set_test_cookie()
        if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
        else:
            return HttpResponse("Please enable cookies and try again")
        form = NewRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            inp_password = form.cleaned_data['password']
            inp_username = form.cleaned_data['username']
            new_register = form.save(commit=False)
            hashed_password = make_password(inp_password)
            new_register.password = hashed_password
            new_register.save()
            user_object = get_object_or_404(User_info, username=inp_username)
            profile_image = request.FILES['image']
            profile_image_object = ProfileImage(image=profile_image, username=user_object)
            profile_image_object.image.name = inp_username + ".jpg"
            profile_image_object.save()
            request.session['username'] = form.cleaned_data['username']
            request.session['is_loggedin'] = True
            return HttpResponseRedirect('/')
    else:
            form = NewRegisterForm()
    return render_to_response('register/newregister.html', {'form': form}, RequestContext(request))

def profile(request, user_name):
	if 'username' not in request.session or not request.session['username'] == user_name:
		is_loggedin=False
		user_object = get_object_or_404(User_info, username=user_name)
                user_details = user_object.__dict__
                user_form = OtherProfileForm(user_details)
		if 'is_loggedin' in request.session and request.session['is_loggedin']:	
			is_loggedin = True
		return render_to_response('register/other_profile.html',{'is_loggedin':is_loggedin, 'user_form':user_form}, RequestContext(request))
	else:
		user_object = get_object_or_404(User_info, username=user_name)
		user_details = user_object.__dict__
		user_form = ProfileForm(user_details)
		return render_to_response('register/my_profile.html', {'is_loggedin':True, 'username':user_name, 'user_form':user_form}, RequestContext(request))


def change_password(request, user_name):
        error = []
        if 'username' not in request.session or not request.session['username'] == user_name:
               return HttpResponseRedirect('/register/login')

        else:
        	if request.method=='POST':
                	request.session.set_test_cookie()
                	if request.session.test_cookie_worked():
                        	request.session.delete_test_cookie()
               		else:
                        	return HttpResponse("Please enable cookies and try again")
                	form = ChangePasswordForm(request.POST)
                	if form.is_valid():
               		        old_password=request.POST['old_password']
				user_data = User_info.objects.get(username = user_name)
	                        if not user_data:
					return HttpResponseRedirect('/')
				else:
                                	actual_password = user_data.password
                               		if not check_password(old_password,actual_password):
						error.append('Your currect password is not correct')
					else:
                        			new_password=request.POST['new_password']
						confirm_new_password = request.POST['confirm_new_password']
						if not new_password == confirm_new_password:
							error.append('password_do not match')
						else:
							new_hashed_password = make_password(new_password)
							user_data.password = new_hashed_password
							user_data.save()
							return render_to_response('register/success.html',{'username':user_name, 'is_loggedin':True},RequestContext(request))
		else:
			form = ChangePasswordForm()
		return render_to_response('register/change_password.html', {'form':form, 'username':user_name, 'error':error, 'is_loggedin':True}, RequestContext(request))


def mypage(request, user_name):
        if 'username' not in request.session or not request.session['username'] == user_name:
                return HttpResponseRedirect('/register/login')
        else:
		return render_to_response('register/mypages.html',{'username':user_name,'is_loggedin':True}, RequestContext(request))

