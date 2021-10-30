"""Cryptoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeProjects.as_view(), name='home'),
    path('projects/', include('project_reviews.urls')),
    path('news/', include('news.urls')),

    # Аuthentication
    path('Login/', views.loginuser, name='loginuser'),
    path('SingUp/', views.signupuser, name='signupuser'),
    path('Logout/', views.logoutuser, name='logoutuser'),


    # Personal Area
    path('articles/', views.myarticles, name='myarticles'),
    path('articles/create-articles', views.createarticles, name='createarticles'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)