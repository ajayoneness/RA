from rest_framework import serializers
from you.models import category,quotes

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = quotes
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = quotes
        fields = '__all__'

