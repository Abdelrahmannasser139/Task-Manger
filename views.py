from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# View to list tasks
def task_list(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# View to add a new task
def add_task(request):
    if request.method == 'POST':  # When form is submitted
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to task list view
    else:
        form = TaskForm()  # Create a new empty form
    return render(request, 'tasks/add_task.html', {'form': form})

# View to edit a task
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)  # Retrieve the task or 404 if not found
    if request.method == 'POST':  # When form is submitted
        form = TaskForm(request.POST, instance=task)  # Prepopulate form with task data
        if form.is_valid():
            form.save()  # Save the edited task to the database
            return redirect('task_list')  # Redirect to task list view
    else:
        form = TaskForm(instance=task)  # Create form prepopulated with task data
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

# View to delete a task
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)  # Retrieve the task or 404 if not found
    if request.method == 'POST':  # If form is submitted to delete
        task.delete()  # Delete the task from the database
        return redirect('task_list')  # Redirect to task list view
    return render(request, 'tasks/delete_task.html', {'task': task})
