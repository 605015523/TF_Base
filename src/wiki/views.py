from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import TfRoles
from datetime import datetime


# Create your views here.
def wiki_index(request):
#    return render(request, 'wiki/index.html')
    template = get_template("wiki/index.html")
    roles = TfRoles.objects.all()
    now = datetime.now()
    html = template.render(locals())
    
    return HttpResponse(html)

