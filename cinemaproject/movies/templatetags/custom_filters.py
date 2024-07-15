from django import template

register = template.Library()

@register.filter(name='truncate_chars')
def truncate_chars(value, max_length):
	if len(value) >= max_length:
		return value[:max_length] + '...'
	return value