from django.shortcuts import render
from .models import *

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Homepage")


def home(request):

    homeitems = Home.objects.all()
    return render(request, "index.html", {'items': homeitems})


def about(request):

    backimg = BackgroundNav.objects.all()
    aboutitems = About.objects.all()
    # return response with template and context
    return render(request, "about.html", {'items': aboutitems, 'background': backimg})


def work(request):

    aboutwork = Whatwedo.objects.all()
    # return response with template and context
    return render(request, "work.html", {'items': aboutwork})


def story(request):

    aboutstory = Story.objects.all()
    adopters = Adopters.objects.all()
    # return response with template and context
    return render(request, "story.html", {'items': aboutstory, 'adopters': adopters})


def adopt(request):

    adoptions = Adoption.objects.all()
    # return response with template and context
    return render(request, "adoption.html", {'adoptions': adoptions})


def contact(request):

    # return response with template and context
    return render(request, "contact.html")


def donate(request):

    donate = Donation.objects.all()
    # return response with template and context
    return render(request, "donation.html", {'donate': donate})

def term(request):

    # return response with template and context
    return render(request, "terms.html")

def privacy(request):

    # return response with template and context
    return render(request, "privacy.html")

def refund(request):

    # return response with template and context
    return render(request, "refund.html")
