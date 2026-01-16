from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import CreateTaskForm

# just a test function
def add(a, b, **extras):
    return a+b

@login_required
def ListAllTasksView(request):

    print(request.user)

    tasks = Task.objects.all().order_by('-created_at')
    messages.success(request, message="ALL Task Listed..")

    return render(request,
            template_name="list_all_task.html",
            context={'tasks':tasks},
            status=200,
        )

@login_required
def TaskDetail(request, id):

    task = get_object_or_404(Task, id=id)

    return render(request, 'detail_task.html', context={'task':task})

@login_required
def CreateTask(request):

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)

        if form.is_valid():
            # data = form.cleaned_data
            # Task.objects.create(**data)
            form.save()

        messages.success(request, message="Task Created Successfully!")

        return redirect('tasks:list_task')
    else:
        form = CreateTaskForm()

    return render(request, 'addtask.html', context={'form':form})

@login_required
def EditTask(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

        messages.success(request, "Task Updated successfully..")
        return redirect('tasks:detail', id=id)
    else:
        form = CreateTaskForm(instance=task)

    return render(request, 'edit.html', context={'form':form})

@login_required
def DeleteTask(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        title = task.title
        task.delete()

        messages.success(request, f"{title}... Task Delete successfully !")
        return redirect('tasks:list_task')

    return render(request, 'delete.html')


