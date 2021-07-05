from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('accounts.urls')),
                  path('', include('home.urls')),
                  path('', include('tweets.urls')),
                  path('chat/', include('chat.urls')),
                  path("logout/", LogoutView.as_view(), name="logout"),
                  # path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
