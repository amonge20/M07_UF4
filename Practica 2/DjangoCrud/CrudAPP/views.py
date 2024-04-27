from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def teachers(request):
    return HttpResponse("Lista Profesor")
    # Person = list(models.Person.objects.all())
    # nom = Person[0].name

    # id_DB = 1
    # person = models.Person.objects.get(id = id_DB)
    # nom = person.name

def create(request):
    return HttpResponse("Crear Usuario")
    # form = PersonForm()

    # if request.method == 'POST';
        # form = PersonForm(request.POST)
        # if form.is_valid():
        #   form.save()
        #   return redirect('index_one')

    # context = {'form':form}
    # return render(request, 'form.html', context)

def update(request):
    return HttpResponse("Actualizar datos usuario")



def delete(request):
    return HttpResponse("Eliminar Usuario")