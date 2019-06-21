from django.contrib import admin
from resume.models import  Employer, Position, BulletPoint, Skill, Education, Award
# Register your models here.

admin.site.register(Employer)
admin.site.register(Position)
admin.site.register(BulletPoint)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Award)