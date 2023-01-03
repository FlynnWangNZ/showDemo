from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from decode.models import ProjectModel


class DecodeView(View):
    def get(self, requests):
        # get all valid projects from database
        projects = ProjectModel.objects.all()

        return render(requests, 'decode.html', {
            'projects': projects
        })

    def post(self, requests):
        project = requests.POST.get('project')
        hex_code = requests.POST.get('hexCode')
        return JsonResponse({"project": project, "hex_code": hex_code}, safe=False)
