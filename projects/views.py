from django.shortcuts import render
from projects.models import  Project

# Create your views here.

def projects(request):
    """View function for home page of site."""

    # Retreive models
    projects = Project.objects.filter(hide=False)

    context = {
        'projects': projects
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'projects.html', context=context)