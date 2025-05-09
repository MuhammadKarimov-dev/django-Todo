from django.shortcuts import render,redirect
from .models import Todo


def indexView(request):

    todoList = Todo.objects.all()
    

    context = {
        "todos": todoList
    }
    return render(request, 'index.html',context)

def todoDoneView(request, id):
    todo = Todo.objects.get(id=id)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()

    return redirect("index")

def todoDeleteView(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("index")
    

def todoCreateView(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        must_be_done = request.POST.get("must_be_done")
        Todo.objects.create(title=title, description=description, must_be_done=must_be_done)
        return redirect("index")