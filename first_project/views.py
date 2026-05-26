# views.py file is created by me.

from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Nameste, Bharat. Welcome you all Django with Raj Home page")
    return render(request, 'index.html')

def About(request):
    # return HttpResponse("Nameste, Bharat. Welcome you all Django with Raj About page")
    return render(request, 'about.html')

def Query(request):
    return HttpResponse("Nameste Bharat. Ask your Doubghts")

def Contact(request):
    return HttpResponse("Nameste Connections, This is Our Contact page")

def Review(request):
    return render(request, 'review.html')