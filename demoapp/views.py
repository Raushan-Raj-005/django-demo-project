from django.shortcuts import render

def all_project(request):
    return render(request, 'demoapp/all_project.html')