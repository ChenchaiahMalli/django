from django.urls import path
from . import views

urlpatterns = [
    path('getTimeStories/', views.get_time_stories, name='get_time_stories'),
    path('', views.home, name='home'),  # Root URL for the homepage
]
