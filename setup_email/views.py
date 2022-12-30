import logging

from django.http import JsonResponse, QueryDict
from django.shortcuts import render


# Create your views here.
from django.views import View

from setup_email.utils import get_svn_version
from showDemo.settings import COMPONENTS


class SetupEmailView(View):
    def get(self, requests):

        return render(requests, 'setup_email/index.html', {
            'components': COMPONENTS
        })

    def post(self, requests):
        # 1. get all parameters from post request

        # 2. validation of parameters

        # 3. fill up the html email template and send it out

        # 4. get everything logged

        # 5. write data to database
        return render(requests, 'setup_email/index.html', {
            'components': COMPONENTS
        })

    def put(self, requests):
        parameters = QueryDict(requests.body)
        component_index = parameters.get('component_index')
        svn_version = get_svn_version(component_index)
        return JsonResponse({'msg': svn_version}, safe=False)
