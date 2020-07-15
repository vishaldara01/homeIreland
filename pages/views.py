from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,   
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blog.html')

def register(request):
    return render(request, 'pages/register.html')

def elements(request):
    return render(request, 'pages/elements.html')

def property_details(request):
    return render(request, 'pages/property_details.html')

def Property(request):
    return render(request, 'pages/Property.html')

def single_blog(request):
    return render(request, 'pages/single_blog.html')