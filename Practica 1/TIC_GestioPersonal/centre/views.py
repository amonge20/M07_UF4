from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Alumnes y Profesors")

def studentsApp(request):
    context = {"students": LlistaAlumnes.values()}
    return render(request, 'studentsApp.html', context)

def teachersApp(request):
    context = {"teachers": LlistaProfes.values()}
    return render(request, 'teachersApp.html', context)

def studentsProject(request):
    context = {"students": LlistaAlumnes.values()}
    return render(request, 'studentsProject.html', context)

def teachersProject(request):
    context = {"teachers": LlistaProfes.values()}
    return render(request, 'teachersProject.html', context)

def alumne(request, pk):
    alumne_Obj = None
    for alumne_key, alumne_data in LlistaAlumnes.items():
        if alumne_data['id'] == int(pk):
            alumne_Obj = alumne_data
            break  
    return render(request, 'student.html', {'student': alumne_Obj})

def profesor(request, pk):
    profesor_Obj = None
    for profesor_key, profesor_data in LlistaProfes.items():
        if profesor_data['id'] == int(pk):
            profesor_Obj = profesor_data
            break  
    return render(request, 'teacher.html', {'teacher': profesor_Obj})


LlistaProfes = {
    'profe1': {
        'id': 1,
        'nom':'Josep Oriol',
        'cognom1':'Roca',
        'cognom2':'Fabra',
        'correu':'joseporiol.roca@iticbcn.cat',
        'curs':'DAW2',
        'ModulsMatriculats':'PHP i Python'
    },
    'profe2': {
        'id': 2,
        'nom':'Juanma',
        'cognom1':'Sanchez',
        'cognom2':'Bel',
        'correu':'juanmanuel.sanchez@iticbcn.cat',
        'curs':'DAW2',
        'ModulsMatriculats':'JavaScript'
    },
    'profe3': {
        'id': 3,
        'nom':'Pere',
        'cognom1':'Guitart',
        'cognom2':'Colom',
        'correu':'pere.guitart@iticbcn.cat',
        'curs':'DAW1',
        'ModulsMatriculats':'Programacio Java'
    }
}

LlistaAlumnes = {
    'alumne1': {
        'id': 1,
        'nom':'Aitor',
        'cognom1':'Monge',
        'cognom2':'Santiago',
        'correu':'2023_aitor.monge@iticbcn.cat',
        'curs':'DAW2',
        'tutor':'Josep Oriol Roca Fabra',
        'ModulsImpartits':'PHP i Python'
    },
    'alumne2': {
        'id': 2,
        'nom':'Didac',
        'cognom1':'Pujol',
        'cognom2':'Perez',
        'correu':'Didac@gmail.com',
        'curs':'DAW1',
        'tutor':'Pere Guitart Colom',
        'ModulsImpartits':'Programacio Java'
    },
    'alumne3': {
        'id': 3,
        'nom':'Alex',
        'cognom1':'Bernades',
        'cognom2':'Ruiz',
        'correu':'Alex@gmail.com',
        'curs':'DAM1',
        'tutor':'Juanma Sanchez Bel',
        'ModulsImpartits':'JavaScript'
    }
}