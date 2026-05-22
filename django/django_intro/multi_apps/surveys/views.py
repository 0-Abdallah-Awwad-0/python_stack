from django.shortcuts import render ,HttpResponse,redirect

# Create your views here.
# this method when called will return http response as a string
def display_survey(request):
    return HttpResponse("placeholder to display all the surveys created.")

# this method will also return http response as a string 
def new_display(request):
    return HttpResponse("placeholder for users to add a new survey.")
