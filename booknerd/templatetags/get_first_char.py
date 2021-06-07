from django import template

register = template.Library()


def get_first_char(string):
    return string[0]

register.filter('get_first_char', get_first_char)