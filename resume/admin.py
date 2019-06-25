from django.contrib import admin
from resume.models import  Employer, Position, BulletPoint, Skill, Education, Award
# Register your models here.



class BulletPointInline(admin.TabularInline):
    model = BulletPoint

admin.site.register(Employer)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Award)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_filter = ('hide',)
    
    inlines = [BulletPointInline]