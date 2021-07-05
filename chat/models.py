from django.db import models
from accounts.models import UserProfile


# Create your models here.

class Messages(models.Model):
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserProfile, related_name='+', on_delete=models.CASCADE)
    message = models.CharField(max_length=500, null=False, blank=False)
    message_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.message


class MessageNotification(models.Model):
    for_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    notification = models.ForeignKey(UserProfile, related_name='+', on_delete=models.CASCADE)
    notification_time = models.DateTimeField(auto_created=True)
    active = models.BooleanField(default=True, )

    def __str__(self):
        return 'New message from user' + f' {self.notification.username} ' + ' for the user ' + self.for_user.username
