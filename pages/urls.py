from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('property_details', views.property_details, name='property_details'),
    path('Property', views.Property, name='Property'),
    path('single_blog', views.single_blog, name='single_blog'),
]