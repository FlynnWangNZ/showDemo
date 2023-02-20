# auth: Flynn Wang
# date: 20/02/23
# desc:


from django.urls import re_path

from grading.views import GradingView

urlpatterns = [
    re_path(r'^$', GradingView.as_view(), name="grading"),
]
