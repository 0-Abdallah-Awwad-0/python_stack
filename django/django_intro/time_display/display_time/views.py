from django.shortcuts import render
from time import gmtime, strftime

# Create your views here. 

#this function will return the time and date to the index    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)