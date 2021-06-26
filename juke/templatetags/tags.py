from django import template
from django.template.defaulttags import register


register = template.Library()

@register.filter
def makeShorterAddy(addy):
    return (addy[:3] + "..." + addy[-4:])

@register.filter
def at(arr, i):
    return arr[i]

@register.filter

def fontSizeFromString(string):
    if len(string) > 30:
        return "1.5rem"
    else:
        return "2.3rem"
