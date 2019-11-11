from django.db import models

# Create your models here.

class Project(models.Model):
    """Model representing a project."""
    name = models.CharField(max_length=40)
    image = models.ImageField()
    image_alt = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    last_modified_date_time = models.DateTimeField(auto_now=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the SocialSite object."""
        return self.name

class ProjectLink(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    link = models.URLField()
