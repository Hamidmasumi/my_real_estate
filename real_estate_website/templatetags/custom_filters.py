# real_estate_website/templatetags/custom_filters.py
from django import template
import re

register = template.Library()

@register.filter(name='is_digit')
def is_digit(value):
    return str(value).isdigit()

@register.filter(name='format_number')
def format_number(value):
    if not isinstance(value, str):
        value = str(value)
    return re.sub(r'\B(?=(\d{3})+(?!\d))', '.', value)