# auth: Flynn Wang
# date: 24/12/22
# desc: url pattern for app setup email


from django.urls import re_path

from setup_email.views import SetupEmailView

urlpatterns = [
    re_path(r'^$', SetupEmailView.as_view(), name="email"),
    # re_path(r'^test/$', test),
]
