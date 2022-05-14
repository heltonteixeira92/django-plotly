from django.urls import path
from . import views


urlpatterns = [
    path('commits/', views.commits, name='commits' )
]