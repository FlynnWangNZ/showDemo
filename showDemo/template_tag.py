# auth: Flynn Wang
# date: 27/12/22
# desc:


from django import template

register = template.Library()


@register.simple_tag
def sidebar():
    return [
        {'name': 'home', 'url': '/home', 'feather': 'home'},
        {'name': 'email', 'url': '/email', 'feather': 'mail'},
        {'name': 'decode', 'url': '/decode', 'feather': 'unlock'},
        {'name': 'job', 'url': '/job', 'feather': 'activity'},
        {'name': 'github', 'url': 'https://github.com/FlynnWangNZ/showDemo', 'feather': 'github'}
    ]
