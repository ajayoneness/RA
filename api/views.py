from rest_framework import generics
from you.models import category,quotes
from .serializers import CategorySerializer, QuotesSerializer,QuoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(['GET'])
def quotes_by_category(request, category_id):
    try:
        quote = quotes.objects.filter(category_id=category_id)
        serializer = QuoteSerializer(quote, many=True)
        return Response(serializer.data)
    except quote.DoesNotExist:
        return Response(status=404)



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
