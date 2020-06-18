from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepass = ''
    length = int(request.GET.get("length"))
    if request.GET.get("uppercase"):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get("number"):
        characters.extend('123456789')

    if request.GET.get("spchar"):
        characters.extend('!@#$%^&*()')

    for _ in range(length):
        thepass += random.choice(characters)

    return render(request, 'generator/password.html', {'pass': thepass})
