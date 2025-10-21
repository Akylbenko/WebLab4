from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleViewSet.as_view({'get': 'list', 'post': 'create'}), name='articles-list'),
    path('articles/<int:pk>/', views.ArticleViewSet.as_view({'get': 'retrieve', 'put': 'update','delete': 'destroy'}), name='articles-detail'),
]