from rest_framework import generics
from .models import SinQuote
from .serializers import SinQuoteSerializer


class ListSinQuote(generics.ListCreateAPIView):
    queryset = SinQuote.objects.all()
    serializer_class = SinQuoteSerializer


class DetailSinQuote(generics.RetrieveUpdateDestroyAPIView):
    queryset = SinQuote.objects.all()
    serializer_class = SinQuoteSerializer
    