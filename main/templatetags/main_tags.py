from django import template
from ..models import Category
register = template.Library()


@register.inclusion_tag('tags/search.html',takes_context=False)
def search_block():
    all_category = Category.objects.all()
    return ({'all_category': all_category})

@register.inclusion_tag('tags/header.html',takes_context=True)
def header_block(context):
    return context

@register.inclusion_tag('tags/post_list.html',takes_context=True)
def post_list(context,post):
    return post
