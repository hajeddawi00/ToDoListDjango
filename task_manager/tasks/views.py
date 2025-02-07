from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
def index_view(request):
    
    tasks = Task.objects.all()

    if request.method == 'POST':
        try:
            new_task = Task(
                name = request.POST['name'],
                is_completed = False
            )
            new_task.save()
            return redirect("tasks:index_view") #prevent reload issue
        except Exception as e:
            print(e)

    return render(request, 'tasks/index.html', {"tasks" : tasks})

def complete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.is_completed = not task.is_completed
        task.save()
    except Task.DoesNotExist:
        return render(request, 'tasks/not_exist.html')
    
    return redirect("tasks:index_view")

def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
    except Task.DoesNotExist:
        return render(request, "tasks/not_exist.html")
    except Exception as e:
        print(e)

    return redirect("tasks:index_view")