from django.shortcuts import render

# Create your views here.
"""def index(request):
    template = 'index.html'
    context = {
        'note_list': [
            {'title': 'Sin noticias de Gurb', 'content': 'Libro de Eduardo Mendoza'},
            {'title': '¿Qué hace un perro con un taladro?', 'content': 'Taladrando'},
        ]
    }
    response = render(request, template, context)
    return response"""

from notes.models import Note
def index(request):
    template = 'index.html'
    context = {
        'note_list': Note.objects.all,
        'note_uno': Note.objects.afirst,
        'filtro_note':Note.objects.filter(title="test1"),
        'portfolio':Note.objects.filter(title="Portfolio"),

        'proyecto1':Note.objects.filter(title="Proyecto1"),
        'proyecto2':Note.objects.filter(title="Proyecto2"),
        'proyecto3':Note.objects.filter(title="Proyecto3"),


    }
    response = render(request, template, context)
    return response

