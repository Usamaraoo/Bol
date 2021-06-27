from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(AbstractUser):
    prof_pic = models.ImageField(upload_to='prof_image', blank=True, null=True)
    prof_cover = models.ImageField(upload_to='prof_cover', blank=True, null=True)
    following = models.ManyToManyField('UserProfile', blank=True, null=True)
    followers = models.ManyToManyField('UserProfile', related_name='+', blank=True, null=True)


class UserNotification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    notification = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    notification_time = models.DateTimeField(auto_created=True)
    tweet = models.ForeignKey("tweets.Tweet", null=True, blank=True, on_delete=models.CASCADE)
    from_user = models.ForeignKey(UserProfile, related_name='+', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.notification
