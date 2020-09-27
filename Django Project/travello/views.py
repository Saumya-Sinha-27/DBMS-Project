from django.shortcuts import render, redirect
from .models import models
from .models import destination
from .models import Desti
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    dests = destination.objects.all()
    return render(request, 'index.html', {'dests':dests});

def loginindex(request, id):
    dests = destination.objects.all()
    desti = destination.objects.filter(desti__user_id=id)

    content={
        'dests':dests,
        'desti':desti
    }

    return render(request, 'loginindex.html', content);



