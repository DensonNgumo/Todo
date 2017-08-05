from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import AddTodoForm

def index(request):
    todos=Todo.objects.all()
    context={
    'todos':todos
    }
    return render(request,'index.html',context)

def details(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    context={
    'todo':todo
    }
    return render(request,'details.html',context)

def add(request):
   
    form=AddTodoForm(request.POST or None)

    if(form.is_valid()):
        title=form.cleaned_data['title']
        text=form.cleaned_data['information']

        todo=Todo(title=title,text=text)
        todo.save()
        return redirect('index')
    else:
         context={'form':form}
         template='add.html'
         return render(request,template,context)
            
    
        
    
   

        
      
