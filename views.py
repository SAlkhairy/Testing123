from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('home'))

def home():
    pass

def registration():
    pass

def user_page():
    pass

def timeline(): # I need to come up with new terminology.
    pass

def search_result():
    pass

def user_settings():
    pass

def user_media():
    pass

def following():
    pass

def followers(): # I seriously need to come up with new terminology.
    pass