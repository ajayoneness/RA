from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('quotes/', views.QuotesListCreateView.as_view(), name='quotes-list-create'),
    path('quotes/<int:pk>/', views.QuotesDetailView.as_view(), name='quotes-detail'),
    path('quotes/by_category/<int:category_id>/', views.quotes_by_category, name='quotes_by_category'),
]
