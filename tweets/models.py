from django.db import models
from accounts.models import UserProfile


# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=500, null=False, blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.ManyToManyField(UserProfile, related_name='+', null=True, blank=True)
    comments = models.IntegerField(default=0)

    twt_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.tweet


class Comment(models.Model):
    comment = models.CharField(max_length=200, null=False, blank=False)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    comment_time = models.DateTimeField(auto_created=True, null=True, blank=True)

    def __str__(self):
        return self.comment
