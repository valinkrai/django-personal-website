from django.db import models

# Create your models here.
class Bio(models.Model):
    """Model representing a skill."""
    text = models.TextField()
    last_modified_date_time = models.DateTimeField(auto_now=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the Bio object."""
        return self.created_date_time.strftime("%Y/%m/%d, %H:%M:%S")

class CurrentlyDoing(models.Model):
    """Model representing a skill."""
    text = models.TextField(max_length=1000)
    last_modified_date_time = models.DateTimeField(auto_now=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    link = models.URLField(null=True, blank=True)
    done = models.BooleanField()
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the CurrentlyDoing object."""
        return self.text