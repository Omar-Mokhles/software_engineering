from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Subject, Task
from .forms import SubjectForm, TaskForm

@login_required
def home_view(request):
    subjects = Subject.objects.filter(owner=request.user)
    recent_tasks = Task.objects.filter(subject__owner=request.user).order_by('due_date')[:5]
    
    context = {
        'subjects': subjects,
        'recent_tasks': recent_tasks,
    }
    return render(request, 'planner/home.html', context)


@login_required
def subject_list(request):
    subjects = Subject.objects.filter(owner=request.user)
    return render(request, 'planner/subject_list.html', {'subjects': subjects})

@login_required
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk, owner=request.user)
    tasks = subject.tasks.all()
    return render(request, 'planner/subject_detail.html', {'subject': subject, 'tasks': tasks})

@login_required
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.owner = request.user
            subject.save()
            return redirect('planner:subject_list')
    else:
        form = SubjectForm()
    return render(request, 'planner/subject_form.html', {'form': form, 'title': 'Add a new subject'})

@login_required
def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('planner:subject_detail', pk=subject.pk)
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'planner/subject_form.html', {'form': form, 'title': 'Edit subject'})

@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk, owner=request.user)
    if request.method == 'POST':
        subject.delete()
        return redirect('planner:subject_list')
    return render(request, 'planner/subject_confirm_delete.html', {'subject': subject})


@login_required
def task_list(request):
    tasks = Task.objects.filter(subject__owner=request.user).order_by('due_date')
    return render(request, 'planner/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user)
    return render(request, 'planner/task_detail.html', {'task': task})

@login_required
def task_create(request, subject_pk=None):
    initial_data = {}
    if subject_pk:
        subject = get_object_or_404(Subject, pk=subject_pk, owner=request.user)
        initial_data['subject'] = subject

    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('planner:task_list')
    else:
        form = TaskForm(initial=initial_data, user=request.user)

    return render(request, 'planner/task_form.html', {'form': form, 'title': 'Add a new task'})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('planner:task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task, user=request.user)
    return render(request, 'planner/task_form.html', {'form': form, 'title': 'Edit Task'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, subject__owner=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('planner:task_list')
    return render(request, 'planner/task_confirm_delete.html', {'task': task})