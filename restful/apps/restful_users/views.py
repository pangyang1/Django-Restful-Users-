from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'users' : User.objects.all(),
    }
    return render(request, 'restfulusers/index.html', context)

def new(request):
    return render(request, 'restfulusers/new_users.html')

def create(request):
        if request.POST['name'] and request.POST['email']:
            User.objects.adduser(request.POST)
        else:
            print "Nothing added"
        return redirect('restful:index')

def delete(request, id):
    if request.method == 'GET':
        User.objects.delete(id)
    return redirect('restful:index')

def show(request, id):
    return render(request, 'restfulusers/show.html',{'user': User.objects.get(id=id)})

def edit(request):
    return render(request, 'restfulusers/edit.html',{'user': User.objects.get(id=id)})

def update(request, id):
    if request.POST['name'] and request.POST['email']:
        User.objects.update(request.POST, id)
    else:
        print "Nothing update"
    return render(request, 'restfulusers/show.html', {'user': User.objects.get(id=id)})
# Create your views here.
