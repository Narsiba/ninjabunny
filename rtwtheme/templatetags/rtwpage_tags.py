from django import template
from django.db import models
from django.template.defaultfilters import truncatewords_html, stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.core.fields import RichTextField, OrderField
from mezzanine.utils.html import TagCloser

register = template.Library()


@register.filter(name="cut_content")
@stringfilter
def cut_content(content):
    return content[:70]
