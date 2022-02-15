from django.contrib import admin
from .models import (UserProfile, UserNotification)

# Register your models here.
admin.site.register(UserProfile)
# admin.site.register(UserNotification)


class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'active', 'notification', 'from_user')


admin.site.register(UserNotification, UserNotificationAdmin)
