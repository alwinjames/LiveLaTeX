from django.contrib import admin
from livelatex.projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('user','proj_name', 'proj_id', 'added')

admin.site.register(Project, ProjectAdmin)
