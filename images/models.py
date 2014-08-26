from django.db import models
from django.core.files.storage import FileSystemStorage
from register.models import User_info
import os


IMAGE_CHOICE = (
    ('achievement', 'Achievement'), ('contest', 'Contest'), ('conference', 'Conference'), ('outing', 'Outing'),
    ('profile', 'Profile Pic'), ('other', 'Other'))


class Image(models.Model):
    img_id = models.IntegerField(max_length=100, primary_key=True, blank=False, unique=True)
    img_name = models.CharField(max_length=50, blank=False, null=False)
    img_description = models.CharField(max_length=200)
    img_type = models.CharField(max_length=15, choices=IMAGE_CHOICE, blank=False, null=False)
    img = models.ImageField(upload_to='uploads/photo')


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to. This file storage solves overwrite on upload problem.
        """
        if self.exists(name):
            os.remove(os.path.join("", name))
        return name


"""
Model to store profile images of users.
One to one relation with User_info model.
"""


class ProfileImage(models.Model):
    image = models.ImageField(upload_to="images/profile_image/", storage=OverwriteStorage(), blank=False,
                              null=False)
    username = models.ForeignKey(User_info, blank=False, null=False)


