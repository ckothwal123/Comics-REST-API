from django.contrib.auth.models import User, Group
from rest_framework import serializers
from webscrape.models import Comics

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class ComicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comics  
        fields = ('id', 'comic_title', 'comic_link')

    def to_representation(self, instance):
        return super().to_representation(instance)