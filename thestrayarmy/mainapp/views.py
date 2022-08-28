from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello Homepage")


def home(request):
  
    context = {
        "data": "Sometext for home",
        "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "home.html", context)
