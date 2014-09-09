from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from register.models import User_info

# Create your models here.
ACHIEVEMENT_CHOICE = (('acm','ACM_ICPC'),('article','Article'),('contribution','Contribution'),('gsoc','GSoC'),('intern','Internship'),('speaker','Speaker'),('contest','Contest'),('other','Other'))
INTERN_CHOICE = (('internship','Internship'),('masters','Masters'),('exchange student','Exchange programme'))
SPEAKER_CHOICE =(('talk',' Talk'),('demo','Demo'),('workshop','Workshop'), ('paper','Paper Presentation'),('other','Other'))
LEVEL_CHOICE = (('regional','Regional'), ('finals','World-Finals'))

#main class for achievement
class Achievement(models.Model):
	achievement_id = models.IntegerField(max_length=100, primary_key=True, blank=False, unique=True)
	achieve_type = models.CharField(max_length=15, choices=ACHIEVEMENT_CHOICE)
	username = models.ForeignKey(User_info, blank=False, null=False)

#contribution class: type = contribution
class Contribution(models.Model):
    achievement_id = models.ForeignKey(Achievement, blank=False, null=False)
    bug_id = models.IntegerField(max_length=100, blank=False)
    username = models.ForeignKey(User_info, blank=False, null=False)
    org_name = models.CharField(max_length=50, blank=False, null=False)
    bug_url = models.URLField(max_length=200, blank=False, null=False)
    bug_description = models.CharField(max_length=200)

    class Meta:
        unique_together = ('bug_id','org_name')

#Article class: type = article
class Article(models.Model):
    achievement_id = models.ForeignKey(Achievement, blank=False, null=False)
    article_id = models.IntegerField(max_length=100, primary_key=True, blank=False, unique=True)
    username = models.ForeignKey(User_info, blank=False, null=False)
    area = models.CharField(max_length=100, blank=False, null=False)
    magazine_name = models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    publication_date = models.DateField()

#GSoC class: type = gsoc
class Gsoc(models.Model):
    achievement_id = models.ForeignKey(Achievement, blank=False, null=False)
    gsoc_id = models.IntegerField(max_length=100, primary_key=True, blank=False, unique=True)
    username = models.ForeignKey(User_info, blank=False, null=False)
    organisation = models.CharField(max_length=50, blank=False, null=False)
    project_title = models.CharField(max_length=50, blank=False, null=False)
    mentor_name = models.CharField(max_length=20, blank=False, null=False)
    gsoc_url = models.URLField(max_length=200, blank=False, null=False)


#Internship class: type = intern #can be scholarship also
class Intern(models.Model):
    achievement_id = models.ForeignKey(Achievement, blank=False, null=False)
    intern_id = models.IntegerField(max_length=100, primary_key=True, blank=False, unique=True)
    username = models.ForeignKey(User_info, blank=False, null=False)
    place = models.CharField(max_length=50, blank=False, null=False)
    intern_type =  models.CharField(max_length=16, choices=INTERN_CHOICE, blank=False, null=False)
    period = models.CharField(max_length=25, blank=False, null=False)   


#Speaker class: type = speaker
class Speaker(models.Model):
    achievement_id = models.ForeignKey(Achievement, blank=False, null=False)
    talk_id = models.IntegerField(max_length=100, primary_key=True, blank=False, unique=True)
    username = models.ForeignKey(User_info, blank=False, null=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    speaker_type = models.CharField(max_length=15, choices=SPEAKER_CHOICE, blank=False, null=False)
    conference_name = models.CharField(max_length=50, blank=False, null=False)
    speaker_url = models.URLField(max_length=200, blank=False, null=False)
    year = models.IntegerField(max_length=4, blank=False, null=False)


#ACM_ICPC_details class: type = acm
class ACM_ICPC_detail(models.Model):
    achievement_id = models.ForeignKey(Achievement, blank=False, null=False)
    team_name = models.CharField(max_length=25, primary_key=True, blank=False, unique=True)
    username = models.ForeignKey(User_info, blank=False, null=False)
    yr_of_participation = models.IntegerField(max_length=4, blank=False, null=False)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICE, blank=False, null=False)
    ranking = models.IntegerField(max_length=4, blank=False, null=False)
		
    class Meta:
        unique_together = ('team_name','yr_of_participation')

#ACM_ICPC_Participant class; type = acm
class ACM_ICPC_Participant(models.Model):
	yr_of_participation = models.ForeignKey(ACM_ICPC_detail,related_name= 'year', blank=False, null=False)
	team_name = models.ForeignKey(ACM_ICPC_detail, blank=False, null=False, related_name = 'team')
	name = models.CharField(max_length=25, blank=False, null=False)

#Contest_won class: type = contest
#the username(Achievement) is the user who is adding this information , not the participant ;
class Contest_won(models.Model):
	achievement_id = models.ForeignKey(Achievement, blank=False, null=False)
	contest_id = models.IntegerField(max_length=100, primary_key=True, blank=False, null=False)
	contest_name = models.CharField(max_length=50, blank=False, null=False)
	contest_url = models.URLField(max_length=200)
	description = models.CharField(max_length=200)

#Contest_won_participant class: type=contest
class Contest_won_participant(models.Model):
	contest_id = models.ForeignKey(Contest_won, blank=False, null=False)
	name = models.CharField(max_length = 25, blank=False, null=False)

#Miscellaneous class: type=other
class Miscellaneous(models.Model):
	achievement_id = models.ForeignKey(Achievement, blank=False, null=False)
	username = models.ForeignKey(User_info, blank=False, null=False)
	miscellaneous_id = models.IntegerField(max_length=100, primary_key=True, blank=False, null=False)
	description = models.CharField(max_length=200, blank=False, null=False)
