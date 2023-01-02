from django.contrib import admin

# Register your models here.
from setup_email.models import EmailHistoryModel


class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'modify_time']
    list_display_links = list_display
    list_filter = ['user']
    search_fields = ['recipient', 'component', 'jira_issue', 'tested_by', 'is_urgent', 'user']


admin.site.register(EmailHistoryModel, EmailHistoryAdmin)


admin.site.site_header = 'ShowDemo By Flynn'
admin.site.site_title = 'ShowDemo'
