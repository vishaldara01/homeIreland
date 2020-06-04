from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blog.html')

def contact(request):
    return render(request, 'pages/contact.html')

def elements(request):
    return render(request, 'pages/elements.html')

def property_details(request):
    return render(request, 'pages/property_details.html')

def Property(request):
    return render(request, 'pages/Property.html')

def single_blog(request):
    return render(request, 'pages/single_blog.html')