from django import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import HomePage

@processor_for("destinations")
def get_cards(request, page):
    ordered = page.children.order_by("_order")
    published = [ p for p in ordered if p in page.children.published() ]
    cards = [ page for page in published if  hasattr(page,"gallery")
]
    return {'cards': cards}
