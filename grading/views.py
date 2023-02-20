from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View

from grading.models import CourseModel, AssignmentModel


class GradingView(View):
    def get(self, request):
        courses = CourseModel.objects.all()
        return render(request, 'grading.html', context={
            'courses': courses,
        })

    def post(self, request):
        course_id = int(request.POST.get('course_id'))
        assignments = list(AssignmentModel.objects.filter(course_id=course_id).values())
        return JsonResponse(assignments, safe=False)

