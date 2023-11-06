from django.shortcuts import render

# Create your views here.

from .models import *



def index(request):
    bbs = Bb.objects.all()
    return render(request, "btest/index.html", {'bbs': bbs})

