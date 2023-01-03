from django.db import models

# Create your models here.


class ProjectModel(models.Model):
    # FTP/FTDC/FAIR
    project_name = models.CharField(max_length=50, verbose_name='ProjectName')
    project_code = models.CharField(max_length=20, verbose_name='ProjectCode')

    add_time = models.DateTimeField(verbose_name='AddTime', auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name='ModifyTime', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = 'Decode'


