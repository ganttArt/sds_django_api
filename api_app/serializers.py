from rest_framework import serializers
from .models import SinQuote

class SinQuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SinQuote
        fields = ['id', 'sin', 'quote', 'url',]
