from django import template
from ..models import Category
register = template.Library()


@register.inclusion_tag('tags/search.html',takes_context=False)
def search_block():
    all_category = Category.objects.all()
    return {'all_category': all_category}