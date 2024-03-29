"""Defines how pages will get rendered"""
from django.shortcuts import render
from resume.models import  Employer, Skill, Education, Award, Bio
from django.db.models import Max

# Create your views here.

def resume(request):
    """View function for home page of site."""

    # Retreive models
    try:
        bio = Bio.objects.latest('created_date_time')
    except Bio.DoesNotExist:
        bio = None

    employers = Employer.objects.filter(hide=False).annotate(ed=Max('position__end_date')).order_by('-ed')
    skills = Skill.objects.filter(hide=False)
    education = Education.objects.filter(hide=False)
    awards = Award.objects.filter(hide=False)

    context = {
        'title': 'Resume',
        'uri': request.path,
        'bio': bio,
        'employers': employers,
        'skills': skills,
        'education': education,
        'awards': awards
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'resume.html', context=context)
