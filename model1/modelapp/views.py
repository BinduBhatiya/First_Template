#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import myclass

def modelapp(request):
    mymembers = myclass.objects.all().values()
    template = loader.get_template('model_index.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = myclass.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


# Create your views here.
