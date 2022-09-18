
from django.urls import path
# now import the views.py file into this code
from . import views
urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('work', views.work),
    path('stories', views.story),
    path('adopt', views.adopt),
    path('contact', views.contact),
    path('donate', views.donate),
    path('terms', views.term),
    path('privacy', views.privacy),
    path('refund', views.refund),
]
