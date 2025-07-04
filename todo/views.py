from django.shortcuts import render,redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        Todo.objects.create(title=title)
    return redirect('index')

def delete_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        message = 'Todo deleted successfully!'
    except Todo.DoesNotExist:
        message = 'Todo not found!'
    return redirect('index')

def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')

def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST.get('title', todo.title)
        todo.save()
        return redirect('index')
    return render(request, 'todo/edit.html', {'todo': todo})
