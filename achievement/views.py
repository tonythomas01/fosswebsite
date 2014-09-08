# Django libraries
from django.shortcuts import HttpResponseRedirect, render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


# Application specific functions
from achievement.models import *
from achievement.forms import AddContributionForm
from fossWebsite.helper import error_key, csrf_failure, logged_in
from achievement.helper import get_achievement_id


# Create your views here.
def achieve_viewall(request):
	"""
	View to display recent 5 achievements
	"""
	username = ''
	contrib_list = []
	article_list = []
	gsoc_list = []
	speaker_list = []
	intern_list = []
	contest_participant_list = []
	icpc_participant_list = []
	if logged_in(request):
		username = request.session['username']
	contrib_list = Contribution.objects.all()[:5]
	article_list = Article.objects.all()[:5]
	gsoc_list = Gsoc.objects.all()[:5]
	speaker_list = Speaker.objects.all()[:5]
	intern_list = Intern.objects.all()[:5]
	contest_list = Contest_won.objects.all()[:5]
	if contest_list:	
		contest_participant_list = []
		for contest_won_obj in contest_list:	
			c_id = contest_won_obj.contest_id
			c_p_objs = Contest_won_participant.objects.filter(contest_id = c_id)
			contest_participant_list.extend(c_p_objs)
	icpc_list = ACM_ICPC_detail.objects.all().order_by('yr_of_participation')[:5]
	if icpc_list:
		for icpc_obj in icpc_list:
			team = icpc_obj.team_name
			i_p_objs = ACM_ICPC_Participant.objects.filter(team_name = team)
			icpc_participant_list.extend(i_p_objs)
		
	return render_to_response('achievement/achievement_viewall.html',\
		{'username':username, 'is_loggedin':logged_in(request), \
		'contrib_list':contrib_list, 'article_list':article_list, \
		'gsoc_list':gsoc_list, 'speaker_list':speaker_list, \
		'intern_list':intern_list, 'contest_list':contest_list, \
		'contest_participant_list':contest_participant_list, \
		'icpc_list':icpc_list, 'icpc_participant_list':icpc_participant_list} \
		,RequestContext(request))

def contrib_viewall(request):
	"""
	View to display all contributions
	"""
	username = ''
	if logged_in(request):
		username = request.session['username']
	contrib_list = Contribution.objects.all()
	if contrib_list:
		return render_to_response('achievement/contrib_viewall.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'contrib_list':contrib_list}, \
			RequestContext(request))
	else:
		return render_to_response('achievement/noview.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'type': 'Contribution'}, \
			RequestContext(request))

def article_viewall(request):
	"""
	View to display all articles published
	"""
	username = ''
	if logged_in(request):
		username = request.session['username']
	article_list = Article.objects.all()
	if article_list:
		return render_to_response('achievement/article_viewall.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'article_list':article_list}, \
			RequestContext(request))
	else:
		return render_to_response('achievement/noview.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'type': 'Article'}, \
			RequestContext(request))


def gsoc_viewall(request):
	"""
	View to display all GSOCers
	"""
	username = ''
	if logged_in(request):
		username = request.session['username']
	gsoc_list = Gsoc.objects.all()
	if gsoc_list:
		return render_to_response('achievement/gsoc_viewall.html', \
			{'is_loggedin':loggedin(request), \
			'username':username, \
			'gsoc_list':gsoc_list}, \
			RequestContext(request))
	else:
		return render_to_response('achievement/noview.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'type': 'Gsoc'}, \
			RequestContext(request))


def speaker_viewall(request):
	"""
	View to display all Speakers
	"""
	username = ''
	if logged_in(request):
		username = request.session['username']
	speaker_list = Speaker.objects.all()
	if speaker_list:
		return render_to_response('achievement/speaker_viewall.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'speaker_list':speaker_list}, \
			RequestContext(request))
	else:
		return render_to_response('achievement/noview.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'type': 'Speaker'}, \
			RequestContext(request))

def intern_viewall(request):
	"""
	View to display all internships done
	"""
	username = ''
	if logged_in(request):
		username = request.session['username']
	intern_list = Intern.objects.all()
	if intern_list:
		return render_to_response('achiievement/intern_viewall.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'intern_list':intern_list}, \
			RequestContext(request))
	else:
		return render_to_response('achievement/noview.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'type': 'Internship'}, \
			RequestContext(request))

def contest_won_viewall(request):
	"""
	View to display all Contest Won
	"""
	username = ''
	if logged_in(request):
		username = request.session['username']
	contest_list = Contest_won.objects.all()
	if contest_list:	
		contest_participant_list = []
		for contest_won_obj in contest_list:	
			c_id = contest_won_obj.contest_id
			c_p_objs = Contest_won_participant.objects.filter(contest_id = c_id)
			contest_participant_list.extend(c_p_objs)
		return render_to_response('achievement/contest_viewall.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'contest_list':contest_list, \
			'contest_participant_list':contest_participant_list}, \
			RequestContext(request))
	else:
		return render_to_response('achievement/noview.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'type': 'Contest\'s won'}, \
			RequestContext(request))

def icpc_viewall(request):
	"""
	View to display all ICPCers.
	"""
	username = ''
	if 'is_loggedin' in request.session:
		username = request.session['username']
	icpc_list = ACM_ICPC_detail.objects.all().order_by('yr_of_participation')
	if icpc_list:
		icpc_participant_list = []
		for icpc_obj in icpc_list:
			team = icpc_obj.team_name
			i_p_objs = ACM_ICPC_Participant.objects.filter(team_name = team)
			icpc_participant_list.extend(i_p_objs)
		return render_to_response('achievement/icpc_viewall.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'icpc_list':icpc_list, \
			'icpc_participant_list':icpc_participant_list},\
			 RequestContext(request))
	else:
		return render_to_response('achievement/noview.html', \
			{'is_loggedin':logged_in(request), \
			'username':username, \
			'type': 'ACM ICPC Contest'}, \
			RequestContext(request))



def insert_contribution(request):
	"""
	View to add new Contribution.
	Models used: Achievement, Contribution
	"""
	try:
		# User is not logged in
		if not logged_in(request):
			return HttpResponseRedirect('/register/login')
		# User is logged in
		else:
			if request.method == 'POST':
				form = AddContributionForm(request.POST)
			
				# Invalid form imput
				if not form.is_valid():
					error = "Invalid inputs"
					return render_to_response('achievement/new_contribution.html', \
                        {'form': form, 'error':error}, \
                        RequestContext(request))
				# Form is valid
				else:
					# get the new achievement_id
					achievement_id = get_achievement_id(request)
					
					user_name = request.session['username']
					achievement_type = "contribution"
					# Saving inputs
	
					achievement_obj = Achievement(achievement_id, achievement_type, user_name)
					achievement_obj.save()
					contribution_obj = form.save(commit = False)
					contribution_obj.achievement_id = achievement_obj
					contribution_obj.achieve_typ = achievement_type
					user_obj = get_object_or_404(User_info, username = user_name)
					contribution_obj.username = user_obj
					contribution_obj.save()
					return render_to_response('achievement/success.html', \
						{achievement_type:"contribution"},	\
						RequestContext(request))
			# method is not POST
			else:
				return render_to_response('achievement/new_contribution.html', \
                        {'form': AddContributionForm }, \
                        RequestContext(request))
	except KeyError:
		return error_key(request)
		
	
