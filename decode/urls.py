# auth: Flynn Wang
# date: 3/01/23
# desc:

from django.contrib.auth.decorators import login_required
from django.urls import re_path

from decode.views import DecodeView

urlpatterns = [
    re_path(r'^$', login_required(DecodeView.as_view()), name="decode"),
]
