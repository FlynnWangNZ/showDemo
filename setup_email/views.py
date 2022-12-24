from django.shortcuts import render


# Create your views here.

def test(requests):
    print('test method')
    return render(requests, 'setup_email/index.html')
