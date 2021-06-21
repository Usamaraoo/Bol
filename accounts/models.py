from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(AbstractUser):
    prof_pic = models.ImageField(upload_to='prof_image', blank=True, null=True)
    prof_cover = models.ImageField(upload_to='prof_cover', blank=True, null=True)
    following = models.ManyToManyField('UserProfile')
    followers = models.ManyToManyField('UserProfile',related_name='+')
