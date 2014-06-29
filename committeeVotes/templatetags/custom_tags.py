from django import template

register = template.Library()

def active_page(request, view_name):
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return ""
    try:
        return "active" if resolve(request.path_info).url_name in view_name else ""
    except Resolver404:
        return ""

register.simple_tag(active_page)

