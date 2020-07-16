from rest_framework import generics, viewsets
from .models import SinQuote
from .serializers import SinQuoteSerializer


class SinQuoteViewSet(viewsets.ModelViewSet):
    queryset = SinQuote.objects.all()
    serializer_class = SinQuoteSerializer
