from django.urls import path, include
from . import views

app_name = 'project_reviews'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<slug:project_slug>/', views.detail, name='detail'),
]