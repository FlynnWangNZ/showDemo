# auth: Flynn Wang
# date: 3/01/23
# desc:


from django.contrib.auth.decorators import login_required
from django.urls import re_path

from job.views import JobView

urlpatterns = [
    re_path(r'^$', login_required(JobView.as_view()), name="job"),
]
