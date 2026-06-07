from django.shortcuts import render,redirect
from . models import *
# Create your views here.
def index(request):
    context= {
        # this will retrieve all users
        "all_shows": Show.objects.all()
    }
    return render(request,"index.html",context)

def show(request):
    context={
    'show':Show.object.get()
    }
    return render(request,'shows.html',context)

def edit(request):
    context={
    'show':Show.object.get()
    }
    return render(request,'edit.html',context)


def new(request):
    return render(request,"new.html")

def create(request):

    show= Show.objects.create(
        title = request.POST["title"],
        network =request.POST["network"],
        release_date=request.POST["release_date"],
        desc= request.POST["desc"],
    )
    return redirect(f'/shows/{show.id}')

def destroy(request,id):
    show=Show.objects.get(id =id)
    show.delete()
    return redirect('shows')

def update (request,id):
    show=Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network =request.POST["network"]
    show.release_date=request.POST["release_date"]
    show.desc= request.POST["desc"]
    show.save()
    return redirect(f'shows/{show.id}')
