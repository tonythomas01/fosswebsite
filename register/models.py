from django.db import models
# Create your models here.
GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
ROLE_CHOICES = (('S', 'Student'), ('M', 'Mentor'), ('B', 'Both'))
GOAL_CHOICES = (('startup', 'startup'), ('higher_studies', 'Higher Studies'), ('job', 'Job'), ('other', 'Others'))

class User_info(models.Model):
    firstname = models.CharField(max_length=20, blank=False, unique=False)
    lastname = models.CharField(max_length=20, blank=False, unique=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField() 
    contact = models.CharField(max_length=11)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    interest = models.CharField(max_length=200)
    achieve = models.CharField(max_length=200)
    expertise = models.CharField(max_length=200)
    goal = models.CharField(max_length=15, choices=GOAL_CHOICES)
    username = models.CharField(max_length=20, primary_key=True, unique=True, blank=False)
    password = models.CharField(max_length=20, blank=False)
