from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm

# Create your views here.
def users(request):
    filtrarRol = request.GET.get('role', None)
    if filtrarRol == 'profesor':
        listaUsuarios = Person.objects.filter(rol__nom='profesor').order_by('id')
    elif filtrarRol == 'estudiante':
        listaUsuarios = Person.objects.filter(rol__nom='estudiante').order_by('id')
    else:
        listaUsuarios = Person.objects.all().order_by('id')
    return render(request, 'users.html', {'users_list': listaUsuarios})

def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = PersonForm()
    return render(request, 'create.html', {'form': form})

def update(request,pk):
    person = Person.objects.get(id = pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('users')
    
    context = {'form':form}
    return render(request, 'update.html', context)

def delete(request,pk):
    person = Person.objects.get(id = pk)

    if request.method == 'POST':
        person.delete()
        return redirect('users')
    
    context = {'object':person}
    return render(request, 'delete.html', context)