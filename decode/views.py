import logging

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from decode.models import ProjectModel
from decode.utils import DecodeFactory


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
        decode = DecodeFactory(project, hex_code).get_product()
        try:
            code_json = decode.read()
        except Exception as e:
            code_json = {'errMsg': e}
            logging.exception(e)

        return JsonResponse(code_json, safe=False)
