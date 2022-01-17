from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('FirstApp/', views.index, name='index'),
    path('', views.catalog, name='catalog'),
    path('new_page/', views.new_page_link, name='new_page_link')
]