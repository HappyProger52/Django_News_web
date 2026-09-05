from django.urls import path
from .article_controller import ArticleController
from . import views
from .auth_controller import AuthController

urlpatterns = [
    path('', views.home, name='home'),
    path('galery/<int:news_id>/', views.galery, name='galery'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('articles/', ArticleController.index, name='articles'),
    path('signin/', AuthController.signin, name='signin'),
]