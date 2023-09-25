from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('singlepage/<str:slug>',views.singlepost,name='singlepage'),

]
