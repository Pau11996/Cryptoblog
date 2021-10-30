from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from home.forms import AddNews
from news.models import News
from project_reviews.models import Projects
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views.generic import ListView



class HomeProjects(ListView):
    model = Projects
    template_name = 'home/home.html'
    context_object_name = 'projects'
    extra_context = {'title': 'Главная страница'}

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = menu
    #     context['title'] = 'Главная страница'
    #     return context



# def home(request):
#     projects = Projects.objects.all()
#     return render(request, 'home/home.html', {'projects':projects})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'home/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'home/login.html', {'form': AuthenticationForm(), 'error': 'Username and password did not much'})
        else:
            login(request, user)
            return redirect('myarticles')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'home/SingUp.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],  password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('myarticles')
            except IntegrityError:
                return render(request, 'home/SingUp.html', {'form': UserCreationForm(), 'error': 'That usernae has already been taken. Please choise a new username'})
        else:
            return render(request, 'home/SingUp.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})



def myarticles(request):
    return render(request, 'home/myarticles.html')

@login_required
def createarticles(request):
    if request.method == 'POST':
        form = AddNews(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('myarticles')
    else:
        form = AddNews()
    return render(request, 'home/createarticles.html', {'form': form})

