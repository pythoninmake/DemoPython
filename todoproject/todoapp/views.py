from django.shortcuts import render, redirect
from . models import Task
from . forms import TodoForm


# Create your views here.


def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"home.html",{"key1":task1})
# def details(request):
#     task=Task.objects.all()
#     return render(request,"detail.html",{"key1":task})
def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{"key2":f,"key3":task})