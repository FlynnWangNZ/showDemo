from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class JobView(View):
    def get(self, requests):
        return render(requests, 'job.html', {

        })

    def post(self, requests):
        return JsonResponse({}, safe=False)
