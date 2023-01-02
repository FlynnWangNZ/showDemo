from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class DecodeView(View):
    def get(self, requests):
        return render(requests, 'decode/index.html', {

        })

    def post(self, requests):
        return JsonResponse({}, safe=False)
