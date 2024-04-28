from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm

# Create your views here.
def teachers(request):
    teachers_list = Person.objects.filter(rol_id=1).order_by('id')
    return render(request, 'teachers.html', {'teachers_list': teachers_list})

def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')

    else:
        form = PersonForm()
    return render(request, 'crearTeacher.html', {'form': form})

def update(request,pk):
    person = Person.objects.get(id = pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    
    context = {'form':form}
    return render(request, 'actualizarTeacher.html', context)

def delete(request,pk):
    person = Person.objects.get(id = pk)

    if request.method == 'POST':
        person.delete()
        return redirect('teachers')
    
    context = {'object':person}
    return render(request, 'eliminarTeacher.html', context)