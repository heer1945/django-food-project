from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# def home(request):
#     return HttpResponse("this is a home page")                     ##when i want to show this message


def demo(request):
    return render(request,"demo.html")

def home(request):
    return render(request,"home.html")                                ##when we want to show the code written in the home page

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
