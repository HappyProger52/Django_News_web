from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galery/<int:news_id>/', views.galery, name='galery'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]