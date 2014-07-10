from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from achievement.models import *
# Create your views here.

def achieve_viewall(request):
	is_loggedin = False
        username = ''
	contrib_list = []
	article_list = []
	gsoc_list = []
	speaker_list = []
	intern_list = []
	contest_list = []
	contest_participant_list = []
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
        achieve_contrib_list = Achievement.objects.filter(achieve_type = 'contribution')[:5]
        if achieve_contrib_list:
                for a_obj in achieve_contrib_list:
                        achieve_id = a_obj.achievement_id
                        c_obj = get_object_or_404(Contribution, achievement_id = achieve_id)
                        if c_obj:
                                contrib_list.append(c_obj)
	achieve_article_list = Achievement.objects.filter(achieve_type = 'article')[:5]
        if achieve_article_list:
                for a_obj in achieve_article_list:
                        achieve_id = a_obj.achievement_id
                        article_obj = get_object_or_404(Article, achievement_id = achieve_id)
                        if article_obj:
                                article_list.append(article_obj)
        achieve_gsoc_list = Achievement.objects.filter(achieve_type = 'gsoc')[:5]
        if achieve_gsoc_list:
                for a_obj in achieve_gsoc_list:
                        achieve_id = a_obj.achievement_id
                        gsoc_obj = get_object_or_404(Gsoc, achievement_id = achieve_id)
                        if gsoc_obj:
                                gsoc_list.append(gsoc_obj)
        achieve_speaker_list = Achievement.objects.filter(achieve_type = 'speaker')[:5]
        if achieve_speaker_list:
                for a_obj in achieve_speaker_list:
                        achieve_id = a_obj.achievement_id
                        speaker_obj = get_object_or_404(Speaker, achievement_id = achieve_id)
                        if speaker_obj:
                                speaker_list.append(speaker_obj)
	achieve_intern_list = Achievement.objects.filter(achieve_type = 'intern')[:5]
	if achieve_intern_list:
		for a_obj in achieve_intern_list:
			achieve_id = a_obj.achievement_id
			intern_obj = get_object_or_404(Intern, achievement_id = achieve_id)
			if intern_obj:	
				intern_list.append(intern_obj)
	
	achieve_contest_list = Achievement.objects.filter(achieve_type = 'contest')[:5]
	if achieve_contest_list:
		for a_obj in achieve_contest_list:
			achieve_id = a_obj.achievement_id
			contest_won_obj = get_object_or_404(Contest_won, achievement_id = achieve_id)
			if contest_won_obj:	
				c_id = contest_won_obj.contest_id
				c_p_objs = Contest_won_participant.objects.filter(contest_id = c_id)
				contest_participant_list.extend(c_p_objs)
				contest_list.append(contest_won_obj)
	return render_to_response('achievement/achievement_viewall.html',{'username':username, 'is_loggedin':is_loggedin, 'contrib_list':contrib_list, 'article_obj':article_list, 'gsoc_list':gsoc_list, 'speaker_list':speaker_list,'intern_list':intern_list, 'contest_list':contest_list, 'contest_participant_list':contest_participant_list},RequestContext(request))

def contrib_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_obj = Achievement.objects.filter(achieve_type = 'contribution')
	if achieve_obj:
		contrib_list = []
		for a_obj in achieve_obj:
			achieve_id = a_obj.achievement_id
			c_obj = get_object_or_404(Contribution, achievement_id = achieve_id)
			if c_obj:	
				contrib_list.append(c_obj)
		return render_to_response('achievement/contrib_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'contrib_list':contrib_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Contribution'}, RequestContext(request))

def article_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_obj = Achievement.objects.filter(achieve_type = 'article')
	if achieve_obj:
		article_list = []
		for a_obj in achieve_obj:
			achieve_id = a_obj.achievement_id
			article_obj = get_object_or_404(Article, achievement_id = achieve_id)
			if article_obj:	
				article_list.append(article_obj)
		return render_to_response('achievement/article_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'article_list':article_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Article'}, RequestContext(request))


def gsoc_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_obj = Achievement.objects.filter(achieve_type = 'gsoc')
	if achieve_obj:
		gsoc_list = []
		for a_obj in achieve_obj:
			achieve_id = a_obj.achievement_id
			gsoc_obj = get_object_or_404(Gsoc, achievement_id = achieve_id)
			if gsoc_obj:	
				gsoc_list.append(gsoc_obj)
		return render_to_response('achievement/gsoc_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'gsoc_list':gsoc_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Gsoc'}, RequestContext(request))


def speaker_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_obj = Achievement.objects.filter(achieve_type = 'speaker')
	if achieve_obj:
		speaker_list = []
		for a_obj in achieve_obj:
			achieve_id = a_obj.achievement_id
			speaker_obj = get_object_or_404(Speaker, achievement_id = achieve_id)
			if speaker_obj:	
				speaker_list.append(speaker_obj)
		return render_to_response('achievement/speaker_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'speaker_list':speaker_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Speaker'}, RequestContext(request))

def intern_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_obj = Achievement.objects.filter(achieve_type = 'intern')
	if achieve_obj:
		intern_list = []
		for a_obj in achieve_obj:
			achieve_id = a_obj.achievement_id
			intern_obj = get_object_or_404(Intern, achievement_id = achieve_id)
			if intern_obj:	
				intern_list.append(intern_obj)
		return render_to_response('achievement/intern_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'intern_list':intern_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Internship'}, RequestContext(request))

def contest_won_viewall(request):
	is_loggedin = False
	username = ''
        if 'is_loggedin' in request.session:
                if request.session['is_loggedin']:
                        is_loggedin = True
                        username = request.session['username']
	achieve_list = Achievement.objects.filter(achieve_type = 'contest')
	if achieve_list:
		contest_list = []
		contest_participant_list = []
		for a_obj in achieve_list:
			achieve_id = a_obj.achievement_id
			contest_won_obj = get_object_or_404(Contest_won, achievement_id = achieve_id)
			if contest_won_obj:	
				c_id = contest_won_obj.contest_id
				c_p_objs = Contest_won_participant.objects.filter(contest_id = c_id)
				contest_participant_list.extend(c_p_objs)
				contest_list.append(contest_won_obj)
		return render_to_response('achievement/contest_viewall.html',{'is_loggedin':is_loggedin, 'username':username, 'contest_list':contest_list, 'contest_participant_list':contest_participant_list}, RequestContext(request))
	else:
		return render_to_response('achievement/noview.html',{'is_loggedin':is_loggedin, 'username':username, 'type': 'Contest\'s won'}, RequestContext(request))


