from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *

def index(request):
    tasks = task.objects.all()
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form':form}
    return render(request, 'lists.html', context)

def updateTask(request, pk):
	task = task.objects.get(id=pk)

	form = taskForm(instance=task)

	if request.method == 'POST':
		form = taskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)
