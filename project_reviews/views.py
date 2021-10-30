from django.shortcuts import render, get_object_or_404
from .models import Projects


def projects(request):
    projects = Projects.objects.all()
    return render(request, 'project_reviews/project_reviews.html', {'projects':projects})

def detail(request, project_slug):
    project = get_object_or_404(Projects, slug=project_slug)
    return render(request, 'project_reviews/detail.html', {'project':project})
