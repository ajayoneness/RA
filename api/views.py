from rest_framework import generics
from you.models import category,quotes
from .serializers import CategorySerializer, QuotesSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class QuotesListCreateView(generics.ListCreateAPIView):
    queryset = quotes.objects.all()
    serializer_class = QuotesSerializer

class QuotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = quotes.objects.all()
    serializer_class = QuotesSerializer
