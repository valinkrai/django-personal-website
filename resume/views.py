from django.shortcuts import render
from resume.models import  Employer, Position, BulletPoint, Skill, Education, Award

# Create your views here.

def resume(request):
    """View function for home page of site."""

    # Retreive models
    employers = Employer.objects.filter(hide=False)
    
    
    context = {
        'employers': employers
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'resume.html', context=context)