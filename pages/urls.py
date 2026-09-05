from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .auth_controller import AuthController
from .article_controller import ArticleController


urlpatterns = [
    path('', views.home, name='home'),
    path('galery/<int:news_id>/', views.galery, name='galery'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),

    path('register/', AuthController.register_form, name='register'),
    path('register/store/', AuthController.register, name='register_store'),

    path('login/', AuthController.login_form, name='login'),
    path('login/store/', AuthController.login_user, name='login_store'),

    path('logout/', AuthController.logout_user, name='logout'),

    path('articles/', ArticleController.index, name='articles'),
    path('articles/create/', login_required(ArticleController.create, login_url='login'), name='article_create'),
    path('articles/store/', login_required(ArticleController.store, login_url='login'), name='article_store'),
    path('articles/<int:article_id>/', ArticleController.show, name='article_show'),
    path('articles/<int:article_id>/edit/', login_required(ArticleController.edit, login_url='login'), name='article_edit'),
    path('articles/<int:article_id>/update/', login_required(ArticleController.update, login_url='login'), name='article_update'),
    path('articles/<int:article_id>/delete/', login_required(ArticleController.delete, login_url='login'), name='article_delete'),
]