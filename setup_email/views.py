import logging

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse, QueryDict
from django.shortcuts import render
# Create your views here.
from django.views import View

from setup_email.utils import get_svn_version
from showDemo.settings import COMPONENTS, EMAIL_HOST_USER


class SetupEmailView(View):
    def get(self, requests):

        return render(requests, 'setup_email/index.html', {
            'components': COMPONENTS
        })

    def post(self, requests):
        # 1. get all parameters from post request
        parameters_dict = requests.POST
        logging.debug(f'SetupEmailView post {parameters_dict}')
        title = parameters_dict.get('emailTitle').rstrip()
        send_to = parameters_dict.get('sendTo').split()
        user = User.objects.get(username=requests.user)
        send_to.append(user.email)

        # 2. fill up the html email template and send it out
        """There should be an html email template. I just use text to make it simple"""
        email_content = 'Dear All: \n\n'
        for key, value in parameters_dict.items():
            if key in ['sendTo', 'emailTitle', 'csrfmiddlewaretoken']:
                continue
            email_content += f'{key}: {value} \n\n'
        send_mail(title, email_content, EMAIL_HOST_USER, send_to, fail_silently=False)
        # 3. write data to database
        return render(requests, 'setup_email/index.html', {
            'components': COMPONENTS
        })

    def put(self, requests):
        parameters = QueryDict(requests.body)
        component_index = parameters.get('component_index')
        svn_version = get_svn_version(component_index)
        return JsonResponse({'msg': svn_version}, safe=False)
