from django.urls import path 
from . import views

urlpatterns = [
        path('', views.home) #This is used after creatiing the home functions to render the html templates
]