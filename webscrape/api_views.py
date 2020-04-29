from webscrape.models import Comics

from rest_framework.generics import ListAPIView
from webscrape.serializers import ComicsSerializer

class HeartAndBrainList(ListAPIView):
    queryset = Comics.objects.filter(comic_type="heart-and-brain")
    serializer_class = ComicsSerializer

class GarfieldList(ListAPIView):
    queryset = Comics.objects.filter(comic_type="garfield")
    serializer_class = ComicsSerializer