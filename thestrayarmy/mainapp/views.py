from django.shortcuts import render
from .models import *

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Homepage")


def home(request):
    aboutlist = About.objects.all()
    homeitems = Home.objects.all()
    return render(request, "index.html", {'items': homeitems, 'aboutlist': aboutlist})


def about(request):
    aboutHero = AboutHero.objects.all()
    aboutitems = About.objects.all()
    # return response with template and context
    return render(request, "about.html", {'items': aboutitems, 'backimg': aboutHero[0]})


def work(request):
    whatwedoHero = WhatwedoHero.objects.all()
    aboutwork = Whatwedo.objects.all()
    # return response with template and context
    return render(request, "work.html", {'items': aboutwork, 'backimg': whatwedoHero[0]})


def story(request):
    storyHero = StoryHero.objects.all()
    aboutstory = Story.objects.all()
    adopters = Adopters.objects.all()
    # return response with template and context
    return render(request, "story.html", {'items': aboutstory, 'adopters': adopters, 'backimg': storyHero[0]})


def adopt(request):
    upForAdoptionHero = UpForAdoptionHero.objects.all()
    adoptions = Adoption.objects.all()
    # return response with template and context
    return render(request, "adoption.html", {'adoptions': adoptions, 'backimg': upForAdoptionHero[0]})


def contact(request):
    contactUsHero = ContactUsHero.objects.all()
    # return response with template and context
    return render(request, "contact.html", {'backimg': contactUsHero[0]})


def donate(request):
    donateHero = DonateHero.objects.all()
    donate = Donation.objects.all()
    # return response with template and context
    return render(request, "donation.html", {'donate': donate, 'backimg': donateHero[0]})

def term(request):
    termsHero = TermsHero.objects.all()
    # return response with template and context
    return render(request, "terms.html", {'backimg': termsHero[0]})

def privacy(request):
    privacyHero = PrivacyHero.objects.all()
    # return response with template and context
    return render(request, "privacy.html", {'backimg': privacyHero[0]})

def refund(request):
    refundHero = RefundHero.objects.all()
    # return response with template and context
    return render(request, "refund.html", {'backimg': refundHero[0]})
