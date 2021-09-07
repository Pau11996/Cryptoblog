from django.urls import path, include
from . import views

app_name = 'project_reviews'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_reviews_id>/', views.detail, name='detail'),
]