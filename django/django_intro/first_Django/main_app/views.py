from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse

# Create your view(s here.
def root(request):
    return redirect("/blogs")

# method index
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

# method new
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

# this one will redirect for the landing page
def create(request):
    return redirect("/")

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect("/blogs")

# the java script object response 
def jres(request):
    book={
        "title" : "Coffe",
        "content" : "Arabica",
    }
    return JsonResponse(book)