from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_task(req):
    if req.method=='POST':
        form = forms.TaskForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('task:add_task')
    else:
        form = forms.TaskForm()
    return render(req, './task/add_task.html', {'form':form})

def show_task(req):
    tasks = models.TaskModel.objects.all()
    return render(req, './task/show_task.html',{'tasks':tasks})

def edit_task(req, id):
    task = models.TaskModel.objects.get(pk=id)
    if req.method=='POST':
        form =forms.TaskForm(req.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:show_task')
        
    form =forms.TaskForm(instance=task)
    return render(req, './task/edit_task.html',{'form':form})

def delete_task(req, id):
    models.TaskModel.objects.get(pk=id).delete()
    return redirect('task:show_task')