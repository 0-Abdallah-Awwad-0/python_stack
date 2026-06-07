from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('guess', views.guess, name='guess'),
    path('reset', views.reset, name='reset'),
    path('save_winner', views.save_winner, name='save_winner'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
]