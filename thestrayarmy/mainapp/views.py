from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Homepage")


def home(request):

    # return response with template and context
    return render(request, "index.html")


def about(request):

    # return response with template and context
    return render(request, "about.html")


def work(request):

    # return response with template and context
    return render(request, "work.html")


def story(request):

    # return response with template and context
    return render(request, "story.html")


def adopt(request):

    # return response with template and context
    return render(request, "adoption.html")


def contact(request):

    # return response with template and context
    return render(request, "contact.html")


def donate(request):

    # return response with template and context
    return render(request, "donation.html")
def term(request):

    # return response with template and context
    return render(request, "terms.html")
def privacy(request):

    # return response with template and context
    return render(request, "privacy.html")
def refund(request):

    # return response with template and context
    return render(request, "refund.html")
