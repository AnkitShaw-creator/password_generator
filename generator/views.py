from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator_templates/home.html')

def about(request):
    return render(request, 'generator_templates/about.html')




def password(request):

    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    lowercase = request.GET.get('lowercase')
    numbers= request.GET.get('numbers')
    special = request.GET.get('special')

    char_lower = list('abcdefghijklmnopqrstuvwxyz')
    char_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    char_numbers = list("0123456789")
    char_special = list('!@#$%^&*+~`')

    lst = []
    if lowercase:
        lst.extend(char_lower)
    if uppercase:
        lst.extend(char_upper)
    if numbers:
        lst.extend(char_numbers)
    if special:
        lst.extend(char_special)

    gen_password = ''
    for x in range(length):
        gen_password += random.choice(lst)
    print(gen_password)
    return render(request, 'generator_templates/password.html', {'password':gen_password})