from django.urls import include, path
from rest_framework import routers
from webscrape import views

urlpatterns = [
    path("heart-and-brain", views.heartAndBrain, name="heart-and-brain"),
    ]
