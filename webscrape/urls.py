from django.urls import include, path
from rest_framework import routers
from webscrape import views, api_views

urlpatterns = [
    path("heart-and-brain", api_views.HeartAndBrainList.as_view(), name="heart-and-brain"),
    path("garfield", api_views.GarfieldList.as_view(), name="garfield"),
    ]
