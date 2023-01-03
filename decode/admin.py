from django.contrib import admin

# Register your models here.
from decode.models import ProjectModel


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_code', 'project_name']
    list_display_links = list_display
    list_filter = ['project_name']
    search_fields = ['project_code', 'project_name']


admin.site.register(ProjectModel, ProjectAdmin)


