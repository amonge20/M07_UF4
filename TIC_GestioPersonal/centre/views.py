from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    profesor = {"name":"Aitor","surname":"Monge","age":"22"}
    template = loader.get_template('index.html')
    dades = template.render({'nombre':profesor["name"], 'apellido':profesor["surname"], 'edad':profesor["age"]})
    return HttpResponse(dades)

def about(request):
    return HttpResponse("about")