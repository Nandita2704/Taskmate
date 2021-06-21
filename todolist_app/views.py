from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import Tasklist, Contect
from todolist_app.form import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required                                    


@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)

        if form.is_valid():

          instance = form.save(commit=False) 
          instance.manage = request.user  
          instance.save()
        messages.success(request,("New Task Added!"))    
        return redirect('todolist')

    else:
        all_tasks = Tasklist.objects.filter(manage = request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def delete_task(request, task_id):
    task = Tasklist.objects.get(pk=task_id)
    
    if task.manage == request.user :
        task.delete()
    else :
        messages.error(request,("Access Restricted, You Are Not Allowed !!"))
    return redirect('todolist')


def edit_task(request, task_id):

    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)  
        form = Taskform(request.POST or None, instance = task)

        if form.is_valid():
            form.save()
            messages.success(request,("Task Edited!")) 
            return redirect('todolist')

    else : 

        tasks_obj = Tasklist.objects.get(pk=task_id) 
        return render(request, 'edit.html', { 'tasks_obj': tasks_obj })


def complete_task(request, task_id):


    task = Tasklist.objects.get(pk=task_id)

    if task.manage == request.user : 
        task.done = True
        task.save()

    else :

        messages.error(request,("Access Restricted, You Are Not Allowed !!"))

    return redirect('todolist')

@login_required
def panding_task(request, task_id):


    task = Tasklist.objects.get(pk=task_id) 

    task.done = False

    task.save()
    return redirect('todolist')    


def index(request):

    #return HttpResponse("Welcome to taskpage")


    context =  {
                 'index_text':"Welcome to Home page.",
                }
    return render(request, 'index.html', context)    


def contect(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '') 
        email = request.POST.get('email', '') 
        phone = request.POST.get('phone', '') 
        enquiry = request.POST.get('enquiry', '')  

        contect = Contect(first_name=first_name, last_name=last_name, email=email, phone=phone, enquiry=enquiry) 
        contect.save()
    return render(request, 'contect.html')


def about(request):
    #return HttpResponse("Welcome to taskpage")
    context =  {
                 'about_text':"Welcome to about page.",
                }
    return render(request, 'about.html', context)

