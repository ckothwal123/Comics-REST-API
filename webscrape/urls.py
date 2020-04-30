from django.urls import include, path
from rest_framework import routers
from webscrape import views

urlpatterns = [
    path("", views.api_root, name="comic_links"),
    path("heart-and-brain/", views.HeartAndBrainList.as_view(), name="heart-and-brain"),
    path("garfield/", views.GarfieldList.as_view(), name="garfield"),
]
