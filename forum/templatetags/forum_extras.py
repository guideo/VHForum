from django import template

register = template.Library()

@register.filter(name='replace_char')
def replace_char(value, arg):
	return value.replace(arg, '')
	
@register.filter
def keyvalue(dict, key):    
    return dict[key]
	
#register.filter('replace_char', replace_char)