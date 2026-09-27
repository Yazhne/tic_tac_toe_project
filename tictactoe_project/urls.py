from django.contrib import admin
from django.urls import path, include  # include is very important

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', include('game.urls')),   # All game app URLs go here
]
