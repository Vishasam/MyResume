from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

def index(request):
    template =loader.get_template('Ai.html')
    return HttpResponse(template.render())