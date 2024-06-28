from django.shortcuts import render
from .models import Page


def page_links(request):
    pages = Page.objects.all()
    return render(request, 'page_links.html', {'pages': pages})

def page_view(request, page_id):
    page = Page.objects.get(id=page_id)
    return render(request, 'page.html', {'page': page})
