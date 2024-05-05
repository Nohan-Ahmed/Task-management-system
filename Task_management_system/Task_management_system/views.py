from django.shortcuts import redirect, render

def home(req):
    return redirect('task:show_task')