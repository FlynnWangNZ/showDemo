from django.contrib import admin

from grading.models import CourseModel, AssignmentModel


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'semester', 'start_date', 'end_date']
    list_display_links = list_display


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'marks', 'percentage', 'course']
    list_display_links = list_display
    list_filter = ['course']


admin.site.register(CourseModel, CourseAdmin)
admin.site.register(AssignmentModel, AssignmentAdmin)
