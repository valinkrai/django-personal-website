"""Defines how pages will get rendered"""
from django.shortcuts import  render
from home.models import  CurrentlyDoing, Bio

# Create your views here.

def home(request):
    """View function for home page of site."""

    # Retreive models
    currently_doing = CurrentlyDoing.objects.filter(hide=False, done=False)
    try:
        bio = Bio.objects.latest('created_date_time')
    except Bio.DoesNotExist:
        bio = None

    context = {
        'title': 'Home',
        'uri': request.path,
        'currently_doing': currently_doing,
        'bio': bio
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)
