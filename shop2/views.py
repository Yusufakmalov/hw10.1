from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home_page(request):
#     return HttpResponse('<h1>Hello<h1/>')

def base_page(request):
    return render(request, 'base.html')
def about_page(request):
    return render(request, 'about.html')