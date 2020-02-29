from django.db import models

# Create your models here.
class SocialSite(models.Model):
    """Model representing a skill."""
    text = models.CharField(max_length=30)
    link = models.URLField()
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the SocialSite object."""
        return self.text