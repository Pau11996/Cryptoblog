from django.urls import path, include
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news, name='news'),
 #   path('<int:blog_id>/', views.detail, name='detail'),
    path('<int:cat_id>/', views.category, name='category'),
]