from django import template

register = template.Library()


def make_list(value):
    return range(value)

register.filter('make_list', make_list)