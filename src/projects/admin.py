from django.contrib import admin
from projects.models import  Project, ProjectLink
# Register your models here.

#admin.site.register(Project)
#admin.site.register(ProjectLink)

class ProjectLinkInline(admin.TabularInline):
    model = ProjectLink


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ('hide',)
    
    inlines = [ProjectLinkInline]