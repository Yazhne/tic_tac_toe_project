from django.urls import path
from . import views  # import views from the app

urlpatterns = [
    path('', views.home, name='home'),         # Home page
    path('play/', views.game, name='game'),    # Human vs Human
    path('ai/', views.ai_game, name='ai_game') # Human vs AI
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),        # Login page as default
    path('play/', views.game, name='game'),          # Human vs Human
    path('ai/', views.ai_game, name='ai_game'),      # Human vs AI
]
