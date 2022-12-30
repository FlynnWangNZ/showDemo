from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class EmailHistoryModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='EmailTitle')
    recipient = models.CharField(max_length=200, verbose_name='SendTo')
    component = models.CharField(max_length=200, verbose_name='Component')
    db_file = models.CharField(max_length=100, verbose_name='DatabaseFile')
    jira_issue = models.CharField(max_length=200, verbose_name='JiraIssue')
    test_report = models.URLField(verbose_name='TestReport')
    tested_by = models.CharField(max_length=10, choices=(('dev', 'dev'), ('qa', 'qa'), ('se', 'se')), verbose_name='TestedBy')
    is_urgent = models.BooleanField(verbose_name='IsUrgent')
    attention = models.CharField(max_length=500, verbose_name='Attention')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    add_time = models.DateTimeField(verbose_name='AddTime', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='ModifyTime', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'EmailHistory'
