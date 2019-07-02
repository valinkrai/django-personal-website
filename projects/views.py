"""Defines how pages will get rendered"""
from django.shortcuts import render
from projects.models import  Project

# Create your views here.

def projects(request):
    """View function for home page of site."""

    # Retreive models
    filtered_projects = Project.objects.filter(hide=False)

    context = {
        'title': 'Projects',
        'uri': request.path,
        'projects': filtered_projects
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'projects.html', context=context)
