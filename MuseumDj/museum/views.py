from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
from .models import Hall, Collection, Exhibit

def index(request): 
    halls = Hall.objects.all() 
    collections = Collection.objects.all() 
    exhibits = Exhibit.objects.all() 
    context = { 'Зал': halls, 'Коллекция': collections, 'Экспонаты': exhibits, } 
    return render(request, "museum/index.html", context)
