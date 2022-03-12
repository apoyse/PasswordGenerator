from django.shortcuts import render
from django.http import HttpResponse
def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'home.html')
# def about(request):
#     return render(request, 'about.html')
# def about(request):
#     return render(request, 'about.html')