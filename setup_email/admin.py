from django.contrib import admin

# Register your models here.
from setup_email.models import EmailHistoryModel


class EmailHistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmailHistoryModel, EmailHistoryAdmin)


admin.site.site_header = 'ShowDemo By Flynn'
admin.site.site_title = 'ShowDemo'
