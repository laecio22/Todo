from django.shortcuts import render, get_object_or_404, redirect
from django .http import HttpResponse
from .models import Task
from .forms import TaskForm


def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk = id)
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):

    if request == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'tasks/addtask.html', {'form': form})


def helloWorld(request):
    return HttpResponse('Hello World !')



def yourName(request, name):
    return render(request,'tasks/yourname.html',{'nome': name})