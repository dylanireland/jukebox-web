from django import template
from django.template.defaulttags import register


register = template.Library()

@register.filter
def makeShorterAddy(addy):
    return (addy[:3] + "..." + addy[-4:])

@register.filter
def at(arr, i):
    return arr[i]
