from django.db import models

# Create your models here.
APPLY_CHOICE = (('scholarship','Scholarship'),('internship','Internship'),('contest','Contest'),('techfest','Tech-Fest'),('others','Others'))

class Apply(models.Model):
	apply_id = models.IntegerField(max_length=100, primary_key=True, blank=False, unique=True)
	name = models.CharField(max_length=50, blank=False, null=False)
	description = models.CharField(max_length=200)
	apply_type = models.CharField(max_length=15, choices=APPLY_CHOICE)
	deadline = models.DateField()
	apply_url = models.URLField(max_length=200, blank=False, null=False) 

