from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def nenusailaja(request):
    return HttpResponse('<h1><marquee>I love you but i am not in love with you</marquee></h1>')