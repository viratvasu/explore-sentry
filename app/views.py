from django.shortcuts import render
from sentry_sdk import capture_exception
from .models import ToDo
def renderTodo(request):
    todos = ToDo.objects.all()
    # print(1/0)
    return render(request,'renderTodos.html',{'todos':todos})

def rendrTodoDetail(request,id):
    context = {}
    try:
        todo_obj = ToDo.objects.get(id = id)
        context['todo']=todo_obj
    except Exception as e:
        capture_exception(e)
    return render(request,'todoDetail.html',context)
def errorEndPoint(request):
    raise Exception("You will get error if you visit this one")
    return render(request,'todoDetail.html')
    
