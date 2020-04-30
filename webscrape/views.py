from django.shortcuts import render
from webscrape.tasks import add, scrape_awkward_yeti
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.reverse import reverse
from webscrape.models import Comics, Titles
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from webscrape.serializers import ComicsSerializer, ComicsTitleSerializer


def homepage_redirect(request):
    return HttpResponseRedirect("/comics/")


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "heart-and-brain": reverse(
                "heart-and-brain", request=request, format=format
            ),
            "garfield": reverse("garfield", request=request, format=format),
        }
    )


class HeartAndBrainList(ListAPIView):
    queryset = Comics.objects.filter(comic_type="heart-and-brain")
    serializer_class = ComicsSerializer


class GarfieldList(ListAPIView):
    queryset = Comics.objects.filter(comic_type="garfield")
    serializer_class = ComicsSerializer


class ComicsList(ListAPIView):
    queryset = Titles.objects.all()
    serializer_class = ComicsTitleSerializer()
