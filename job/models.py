from django.contrib.auth.models import User
from django.db import models


# Job Application Record

# Site Table
# ID, Name, URL
class SourceSiteModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Job Source Site')
    address = models.URLField(verbose_name='Site Address')

    class Meta:
        verbose_name_plural = verbose_name = 'Source Site'

    def __str__(self):
        return self.name


# Record Table
# ID, Date, JobTitle, JobDescription, CompanyName, HREmail, SourceSite, CV, CoverLetter, Details
class JobApplicationRecordModel(models.Model):
    apply_date = models.DateField(verbose_name='Application Date')
    job_title = models.CharField(max_length=100, verbose_name='Job Title')
    job_link = models.URLField(verbose_name='Job Link')
    company_name = models.CharField(max_length=100, verbose_name='Company Name', unique=True, null=False)
    hr_email = models.EmailField(verbose_name='HR Email', null=True, blank=True)
    source_site = models.ForeignKey(SourceSiteModel, on_delete=models.CASCADE, verbose_name='Source Site')
    cv = models.FileField(verbose_name='CV')
    cover_letter = models.FileField(verbose_name='Cover Letter')
    added_by = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = 'Job Application Record'

    def __str__(self):
        return f'{self.job_title} at {self.company_name}'


# Detail Table
# ID, JobDetailID(ForeignKey), Direction(send/receive), Summary, EmailKeyword
class ApplicationDetailModel(models.Model):
    job_detail_id = models.ForeignKey(JobApplicationRecordModel, verbose_name='Job Application ID',
                                      on_delete=models.CASCADE)
    direction = models.IntegerField(verbose_name='Direction', choices=(
        (0, 'send'),
        (1, 'receive')
    ))
    summary = models.CharField(max_length=200, verbose_name='Summary')
    email_keyword = models.CharField(max_length=100, verbose_name='Email Keyword',
                                     help_text='key word to search in the email inbox')
    added_by = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = 'Application Detail'

    def __str__(self):
        return self.summary


# Appointments
# ID, CompanyName, AppointmentTime, IsActive, Feedback, ComingNextWeek
class AppointmentModel(models.Model):
    company_name = models.ForeignKey(JobApplicationRecordModel, to_field='company_name', verbose_name='Company Name',
                                     on_delete=models.CASCADE)
    appointment_time = models.DateTimeField(verbose_name='Appointment Time')
    is_active = models.BooleanField(verbose_name='Is Active', help_text='False if it has been done')
    feed_back = models.TextField(verbose_name='Feedback')
    added_by = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = 'Appointments'

    def __str__(self):
        return f'{self.appointment_time}'
