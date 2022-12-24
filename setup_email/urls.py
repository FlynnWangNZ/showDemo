# auth: Flynn Wang
# date: 24/12/22
# desc: url pattern for app setup email


from django.urls import re_path

from setup_email.views import test

urlpatterns = [
    re_path(r'^test/$', test),
]
