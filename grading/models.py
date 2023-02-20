from django.db import models


# Create your models here.

class CourseModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Course Name')
    semester = models.CharField(max_length=50, verbose_name='Semester')
    start_date = models.DateField(verbose_name='Start Date', null=True, blank=True)
    end_date = models.DateField(verbose_name='End Date', null=True, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = 'Course'

    def __str__(self):
        return self.name


class AssignmentModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Assignment Name')
    marks = models.IntegerField(verbose_name='Marks in Total')
    percentage = models.IntegerField(verbose_name='Percentage')
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, verbose_name='Course Name')

    class Meta:
        verbose_name_plural = verbose_name = 'assignment'

    def __str__(self):
        return self.name
