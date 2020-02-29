"""Defines how pages will get rendered"""
from django.shortcuts import render
from social.models import  SocialSite

# Create your views here.

def social(request):
    """View function for home page of site."""

    # Retreive models
    social_sites = SocialSite.objects.filter(hide=False)

    context = {
        'title': 'Social',
        'uri': request.path,
        'social_sites': social_sites
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'social.html', context=context)