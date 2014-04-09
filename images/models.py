from django.db import models

# Create your models here
IMAGE_CHOICE = (('achievement','Achievement'),('contest','Contest'),('conference','Conference'),('outing','Outing'),('profile','Profile Pic'),('other','Other'))
class Image(models.Model):
	img_id = models.IntegerField(max_length=100, primary_key=True, blank=False, unique=True)
	img_name = models.CharField(max_length=50, blank=False, null=False)
	img_description = models.CharField(max_length=200)
	img_type = models.CharField(max_length=15, choices=IMAGE_CHOICE, blank=False, null=False)
	img = models.ImageField(upload_to='uploads/photo')


