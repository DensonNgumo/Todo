from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def index(request):
    todos=Todo.objects.all()
    context={
    'todos':todos
    }
    return render(request,'todos/index.html',context)

def details(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    context={
    'todo':todo
    }
    return render(request,'todos/details.html',context)

def add(request):
    if(request.method=='POST'):
        title=request.POST['title']
        text=request.POST['text']

        todo=Todo(title=title,text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request,'todos/add.html')