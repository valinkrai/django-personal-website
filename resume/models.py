from django.db import models

# Create your models here.
class Skill(models.Model):
    """Model representing a skill."""
    skill_name = models.CharField(max_length=20)
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the Skill object."""
        return self.skill_name

class Employer(models.Model):
    """Model representing an employer."""
    employer_name = models.CharField(max_length=20)
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the Employer object."""
        return self.employer_name

class Position(models.Model):
    """Model representing an position."""
    employer = models.ForeignKey('Employer', on_delete=models.CASCADE)
    position_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    summary = models.TextField(max_length=500, null=True)
    hide = models.BooleanField()
    
    class Meta:
        ordering = ['end_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.position_name} - {self.employer}'

class BulletPoint(models.Model):
    """Model representing an employer."""
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    blurb = models.TextField(max_length=500)
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the BulletPoint object."""
        return f'{self.position} - {self.blurb[0:70]}'

class Education(models.Model):
    """Model representing an Educational Experience."""
    school_name = models.CharField(max_length=50)
    degree_type = models.CharField(max_length=5)
    degree_field = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=2, decimal_places=1)
    link = models.URLField(null=True)
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the Education object."""
        return f'{self.school_name} - {self.degree_field}'

class Award(models.Model):
    """Model representing an award"""
    event_string = models.CharField(max_length=100)
    link = models.URLField(null=True)
    hide = models.BooleanField()

    def __str__(self):
        """String for representing the Skill object."""
        return self.event_string