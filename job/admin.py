from django.contrib import admin
# Register your models here.
from django.utils.timezone import now

from job.models import SourceSiteModel, JobApplicationRecordModel, ApplicationDetailModel, AppointmentModel


class SourceSiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_display_links = list_display


class JobApplicationRecordAdmin(admin.ModelAdmin):
    list_display = ['apply_date', 'job_title', 'company_name', 'hr_email', 'source_site']
    list_display_links = list_display
    readonly_fields = ['added_by']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(added_by=request.user)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


class ApplicationDetailAdmin(admin.ModelAdmin):
    list_display = ['job_detail_id', 'direction', 'summary', 'email_keyword']
    list_display_links = list_display
    readonly_fields = ['added_by']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(added_by=request.user)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)


class AppointmentAdmin(admin.ModelAdmin):

    def coming_next_week(self, obj):
        return obj.is_active and (obj.appointment_time - now()).days < 7

    list_display = ['company_name', 'appointment_time', 'is_active', 'feed_back', 'coming_next_week']
    list_display_links = list_display
    readonly_fields = ['added_by']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(added_by=request.user)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        obj.save()


admin.site.register(SourceSiteModel, SourceSiteAdmin)
admin.site.register(JobApplicationRecordModel, JobApplicationRecordAdmin)
admin.site.register(ApplicationDetailModel, ApplicationDetailAdmin)
admin.site.register(AppointmentModel, AppointmentAdmin)
