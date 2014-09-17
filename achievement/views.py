# Django libraries
from django.shortcuts import HttpResponseRedirect, render
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


# Application specific functions
from achievement.models import *
from achievement.forms import AddContributionForm, AddArticleForm
from achievement.forms import AddSpeakerForm, AddGSoCForm
from achievement.forms import AddInternForm
from fossWebsite.helper import error_key, csrf_failure, logged_in
from fossWebsite.helper import get_session_variables
from achievement.helper import get_achievement_id


# Create your views here.
def achieve_viewall(request):
    """
    View to display recent 5 achievements
    """
    is_loggedin, username = get_session_variables(request)
    contrib_list = []
    article_list = []
    gsoc_list = []
    speaker_list = []
    intern_list = []
    contest_participant_list = []
    icpc_participant_list = []

    contrib_list = Contribution.objects.all()[:5]
    article_list = Article.objects.all()[:5]
    gsoc_list = Gsoc.objects.all()[:5]
    speaker_list = Speaker.objects.all()[:5]
    intern_list = Intern.objects.all()[:5]
    contest_list = Contest_won.objects.all()[:5]

    
    contrib_org = {}
    if contrib_list:
        for contrib in contrib_list:
            if contrib.org_name not in contrib_org.keys():
                contrib_org[contrib.org_name] = 0

        for contrib in contrib_list:
            contrib_org[contrib.org_name] += 1

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
		{'username':username, \
                'is_loggedin':is_loggedin, \
                'contrib_list':contrib_list, \
                'contrib_org':contrib_org,\
                'article_list':article_list, \
                'gsoc_list':gsoc_list, \
                'speaker_list':speaker_list, \
                'intern_list':intern_list, \
                'contest_list':contest_list, \
                'contest_participant_list':contest_participant_list, \
                'icpc_list':icpc_list, \
                'icpc_participant_list':icpc_participant_list}, \
                RequestContext(request))

def contrib_viewall(request):
    """
    View to display all contributions
    """
    is_loggedin, username = get_session_variables(request)
    contrib_list = Contribution.objects.all()
    
    if contrib_list:
        return render_to_response('achievement/contrib_viewall.html', \
                {'is_loggedin':logged_in(request), \
                'username':username, \
                'contrib_list':contrib_list,}, \
                RequestContext(request))
    else:
        return render_to_response('achievement/noview.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'type': 'Contribution'}, \
                RequestContext(request))

def article_viewall(request):
    """
    View to display all articles published
    """
    is_loggedin, username = get_session_variables(request)
    article_list = Article.objects.all()

    if article_list:
        return render_to_response('achievement/article_viewall.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'article_list':article_list}, \
                RequestContext(request))
    else:
        return render_to_response('achievement/noview.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'type': 'Article'}, \
                RequestContext(request))


def gsoc_viewall(request):
    """
    View to display all GSOCers
    """
    is_loggedin, username = get_session_variables(request)
    gsoc_list = Gsoc.objects.all()

    if gsoc_list:
        return render_to_response('achievement/gsoc_viewall.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'gsoc_list':gsoc_list}, \
                RequestContext(request))
    else:
        return render_to_response('achievement/noview.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'type': 'Gsoc'}, \
                RequestContext(request))


def speaker_viewall(request):
    """
    View to display all Speakers
    """
    is_loggedin, username = get_session_variables(request)
    speaker_list = Speaker.objects.all()

    if speaker_list:
        return render_to_response('achievement/speaker_viewall.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'speaker_list':speaker_list}, \
                RequestContext(request))
    else:
        return render_to_response('achievement/noview.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'type': 'Speaker'}, \
                RequestContext(request))

def intern_viewall(request):
    """
    View to display all internships done
    """
    is_loggedin, username = get_session_variables(request)
    intern_list = Intern.objects.all()

    if intern_list:
        return render_to_response('achievement/intern_viewall.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'intern_list':intern_list}, \
                RequestContext(request))
    else:
        return render_to_response('achievement/noview.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'type': 'Internship'}, \
                RequestContext(request))

def contest_won_viewall(request):
    """
    View to display all Contest Won
    """
    is_loggedin, username = get_session_variables(request)
    contest_list = Contest_won.objects.all()

    if contest_list:	
        contest_participant_list = []
        for contest_won_obj in contest_list:	
            c_id = contest_won_obj.contest_id
            c_p_objs = Contest_won_participant.objects. \
                    filter(contest_id = c_id)
            contest_participant_list.extend(c_p_objs)

        return render_to_response('achievement/contest_viewall.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'contest_list':contest_list, \
                'contest_participant_list':contest_participant_list}, \
                RequestContext(request))
    else:
        return render_to_response('achievement/noview.html', \
                {'is_loggedin':is_loggedin, \
                'username':username, \
                'type': 'Contest\'s won'}, \
                RequestContext(request))

def icpc_viewall(request):
    """
    View to display all ICPCers.
    """
    is_loggedin, username = get_session_variables(request)
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
        is_loggedin, username = get_session_variables(request)
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
                            {'form': form, \
                            'error':error, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))

                # Form is valid
                else:
                    # Get the new achievement_id
                    achievement_id = get_achievement_id(request)	
                    achievement_type = "contribution"

                    # Saving inputs
                    achievement_obj = Achievement(achievement_id, \
                            achievement_type, \
                            username)
                    achievement_obj.save()
                    contribution_obj = form.save(commit = False)
                    contribution_obj.achievement_id = achievement_obj
                    contribution_obj.achieve_typ = achievement_type
                    user_obj = get_object_or_404(User_info, username = username)
                    contribution_obj.username = user_obj
                    contribution_obj.save()
                    return render_to_response('achievement/success.html', \
                            {'achievement_type':achievement_type, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))
            # Method is not POST
            else:
                    return render_to_response('achievement/new_contribution.html', \
                            {'form': AddContributionForm, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))
    except KeyError:
        return error_key(request)


def insert_article(request):
    """
    View to add new Article.
    Models used: Achievement, Article
    """
    try:
        is_loggedin, username = get_session_variables(request)
        # User is not logged in
        if not logged_in(request):
            return HttpResponseRedirect('/register/login')

        # User is logged in
        else:
            if request.method == 'POST':
                form = AddArticleForm(request.POST)

                # Invalid form imput
                if not form.is_valid():
                    error = "Invalid inputs"
                    return render_to_response('achievement/new_article.html', \
                            {'form':form, \
                            'error':error, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))

                # Form is valid
                else:
                    # Get the new achievement_id
                    achievement_id = get_achievement_id(request)	
                    achievement_type = "Article"

                    # Saving inputs
                    achievement_obj = Achievement(achievement_id, \
                            achievement_type, \
                            username)
                    achievement_obj.save()
                    contribution_obj = form.save(commit = False)
                    contribution_obj.achievement_id = achievement_obj
                    contribution_obj.achieve_typ = achievement_type
                    user_obj = get_object_or_404(User_info, username = username)
                    contribution_obj.username = user_obj
                    contribution_obj.save()
                    return render_to_response('achievement/success.html', \
                            {'achievement_type':achievement_type, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))
            # Method is not POST
            else:
                return render_to_response('achievement/new_article.html', \
                        {'form': AddArticleForm, \
                        'is_loggedin':is_loggedin, \
                        'username':username}, \
                        RequestContext(request))
    except KeyError:
        return error_key(request)


def insert_talk(request):
    """
    View to add new talk
    Models used: Achievement, Speaker
    """
    try:
        is_loggedin, username = get_session_variables(request)
        # User is not logged in
        if not logged_in(request):
            return HttpResponseRedirect('/register/login')

        # User is logged in
        else:
            if request.method == 'POST':
                form = AddSpeakerForm(request.POST)

                # Invalid form imput
                if not form.is_valid():
                    error = "Invalid inputs"
                    return render_to_response('achievement/new_speaker.html', \
                            {'form':form, \
                            'error':error, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))

                # Form is valid
                else:
                    # Get the new achievement_id
                    achievement_id = get_achievement_id(request)	
                    achievement_type = "Speaker"

                    # Saving inputs
                    achievement_obj = Achievement(achievement_id, \
                            achievement_type, \
                            username)
                    achievement_obj.save()
                    contribution_obj = form.save(commit = False)
                    contribution_obj.achievement_id = achievement_obj
                    contribution_obj.achieve_typ = achievement_type
                    user_obj = get_object_or_404(User_info, username = username)
                    contribution_obj.username = user_obj
                    contribution_obj.save()
                    return render_to_response('achievement/success.html', \
                            {'achievement_type':achievement_type, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))
            # Method is not POST
            else:
                return render_to_response('achievement/new_speaker.html', \
                        {'form': AddSpeakerForm, \
                        'is_loggedin':is_loggedin, \
                        'username':username}, \
                        RequestContext(request))
    except KeyError:
        return error_key(request)


def insert_gsoc(request):
    """
    View to add gsoc details
    Models used: Achievement, GSoC
    """
    try:
        is_loggedin, username = get_session_variables(request)
        # User is not logged in
        if not logged_in(request):
            return HttpResponseRedirect('/register/login')

        # User is logged in
        else:
            if request.method == 'POST':
                form = AddGSoCForm(request.POST)

                # Invalid form imput
                if not form.is_valid():
                    error = "Invalid inputs"
                    return render_to_response('achievement/new_gsoc.html', \
                            {'form':form, \
                            'error':error, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))

                # Form is valid
                else:
                    # Get the new achievement_id
                    achievement_id = get_achievement_id(request)	
                    achievement_type = "GSoC"

                    # Saving inputs
                    achievement_obj = Achievement(achievement_id, \
                            achievement_type, \
                            username)
                    achievement_obj.save()
                    contribution_obj = form.save(commit = False)
                    contribution_obj.achievement_id = achievement_obj
                    contribution_obj.achieve_typ = achievement_type
                    user_obj = get_object_or_404(User_info, username = username)
                    contribution_obj.username = user_obj
                    contribution_obj.save()
                    return render_to_response('achievement/success.html', \
                            {'achievement_type':achievement_type, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))
            # Method is not POST
            else:
                return render_to_response('achievement/new_gsoc.html', \
                        {'form': AddGSoCForm, \
                        'is_loggedin':is_loggedin, \
                        'username':username}, \
                        RequestContext(request))
    except KeyError:
        return error_key(request)


def insert_intern(request):
    """
    View to add internship details
    Models used: Achievement, Intern
    """
    try:
        is_loggedin, username = get_session_variables(request)
        # User is not logged in
        if not logged_in(request):
            return HttpResponseRedirect('/register/login')

        # User is logged in
        else:
            if request.method == 'POST':
                form = AddInternForm(request.POST)

                # Invalid form imput
                if not form.is_valid():
                    error = "Invalid inputs"
                    return render_to_response('achievement/new_intern.html', \
                            {'form':form, \
                            'error':error, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))

                # Form is valid
                else:
                    # Get the new achievement_id
                    achievement_id = get_achievement_id(request)	
                    achievement_type = "Intern"

                    # Saving inputs
                    achievement_obj = Achievement(achievement_id, \
                            achievement_type, \
                            username)
                    achievement_obj.save()
                    contribution_obj = form.save(commit = False)
                    contribution_obj.achievement_id = achievement_obj
                    contribution_obj.achieve_typ = achievement_type
                    user_obj = get_object_or_404(User_info, username = username)
                    contribution_obj.username = user_obj
                    contribution_obj.save()
                    return render_to_response('achievement/success.html', \
                            {'achievement_type':achievement_type, \
                            'is_loggedin':is_loggedin, \
                            'username':username}, \
                            RequestContext(request))
            # Method is not POST
            else:
                return render_to_response('achievement/new_intern.html', \
                        {'form': AddInternForm, \
                        'is_loggedin':is_loggedin, \
                        'username':username}, \
                        RequestContext(request))
    except KeyError:
        return error_key(request)
