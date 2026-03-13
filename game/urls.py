from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sukida/', views.index2, name='index2'),
    path('banksy/', views.index3, name='index3'),
    path('anniversary/', views.index4, name='index4'),
    path('final/', views.index5, name='index5'),
]
