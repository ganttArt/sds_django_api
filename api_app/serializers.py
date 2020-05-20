from rest_framework import serializers
from .models import SinQuote

class SinQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinQuote
        fields = ['id', 'sin', 'quote']
