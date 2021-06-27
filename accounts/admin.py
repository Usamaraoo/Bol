from django.contrib import admin
from .models import (UserProfile, UserNotification)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserNotification)
