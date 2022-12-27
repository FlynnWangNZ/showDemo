from django.shortcuts import render


# Create your views here.
from showDemo.settings import COMPONENTS


def test(requests):
    print('test method')
    return render(requests, 'setup_email/index.html', {
        'components': COMPONENTS
    })
