from rest_framework import serializers
from webscrape.models import Comics, Titles

# from webscrape.api_views import HeartAndBrainList, GarfieldList


class ComicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ("comic_title", "comic_link")

    def to_representation(self, instance):
        return super().to_representation(instance)


class ComicsTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titles
        fields = ("id", "comic_name")
