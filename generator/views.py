from random import random
from django.shortcuts import render
# from django.http import HttpResponse
import random 



def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'home.html')
def password(request):
    characters = list('abcdefghijklmnopqrstvwxyz')
   
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVWXYZ'))    

    if request.GET.get('specialchar'):
        characters.extend(list('!@#$%^&*~_+-='))   
        
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))   
    
    
    generated_password = ''
    for x in range(length):
        generated_password += random.choice(characters)

    return render (request, 'password.html', { 'password': generated_password})
   

# def about(request):
#     return render(request, 'about.html')