from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characteres = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('mayusculas'):
        characteres.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) 
        
    if request.GET.get('special'):
        characteres.extend(list("<!#$%&**¨¨())"))
    if request.GET.get('numeros'):
        characteres.extend(list("0123456789"))

    length = int(request.GET.get('length'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characteres)

    return render(request, 'generator/password.html',{'password':thepassword})