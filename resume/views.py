"""Defines how pages will get rendered"""
from django.shortcuts import render
from resume.models import  Employer, Skill, Education, Award

# Create your views here.

def resume(request):
    """View function for home page of site."""

    # Retreive models
    employers = Employer.objects.filter(hide=False)
    skills = Skill.objects.filter(hide=False)
    education_experiences = Education.objects.filter(hide=False)
    awards = Award.objects.filter(hide=False)

    context = {
        'employers': employers,
        'skills': skills,
        'education_experiences': education_experiences,
        'awards': awards
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'resume.html', context=context)
