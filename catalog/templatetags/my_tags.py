from django import template

register = template.Library()

@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'

    return '/static/images/notimage.png'


@register.filter()
def mysplit(val):
    return val[:100]

