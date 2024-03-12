from urllib.parse import urlencode

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def order_querystring(context, order_option, field):
    query_dict = context['request'].GET.dict().copy()
    query_dict.update(order=field, dir='asc')
    if order_option.field == field:
        query_dict['dir'] = 'asc' if order_option.direction == 'desc' else 'desc'

    return urlencode(query_dict)


@register.simple_tag
def order_icon(order_option, field):
    if order_option.field != field:
        return ''

    if order_option.direction == 'desc':
        icon = '<i class="bi bi-sort-down-alt"></i>'
    else:
        icon = '<i class="bi bi-sort-up-alt"></i>'

    return mark_safe(icon)


@register.simple_tag(takes_context=True)
def merge_querystring(context, *, exclude_param=None, **kwargs):
    query_dict = context['request'].GET.dict().copy()
    if exclude_param is not None:
        try:
            del query_dict[exclude_param]
        except KeyError:
            pass

    for k, v in kwargs.items():
        query_dict[k] = v

    return urlencode(query_dict)


@register.filter
def split_numbers(nums_string, separator=','):
    return map(int, nums_string.split(separator))

@register.simple_tag(takes_context=True)
def querystring(context, **kwargs):
    """
    Creates a URL (containing only the querystring [including "?"]) derived
    from the current URL's querystring, by updating it with the provided
    keyword arguments.

    Example (imagine URL is ``/abc/?gender=male&name=Tim``)::

        {% querystring "name"="Diego" "age"=20 %}
        ?name=Diego&gender=male&age=20
    """
    request = context['request']
    updated = request.GET.copy()
    for k, v in kwargs.items():
        updated[k] = v

    return f'?{updated.urlencode()}' if updated else ''


@register.simple_tag(takes_context=True)
def order_query_string(context, field):
    ordering = context['request'].GET.get('order')
    if not ordering:
        return ""

    if ordering.startswith('-'):
        field_name = ordering[1:]
        order_dir = ''
    else:
        field_name = ordering
        order_dir = '-'

    if field_name != field:
        return ''

    new_order_field = f'{order_dir}{field_name}'

    return querystring(context, order=new_order_field)


@register.simple_tag(takes_context=True)
def order_querystring(context, order_option, field):
    query_dict = context['request'].GET.dict().copy()
    query_dict.update(order=field, dir='asc')
    if order_option.field == field:
        query_dict['dir'] = 'asc' if order_option.direction == 'desc' else 'desc'

    return urlencode(query_dict)