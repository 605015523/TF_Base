from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import TfRoles, TfStory
from datetime import datetime


# Create your views here.
def wiki_index(request):
    template = get_template("wiki/index.html")
    roles = TfRoles.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def show_content(request, role_id):
    template = get_template("wiki/detail.html")
    try:
        story = TfStory.objects.get(external_id=role_id)
        if story != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/wiki')
