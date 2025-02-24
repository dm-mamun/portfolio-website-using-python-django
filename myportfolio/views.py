from django.shortcuts import render
from .models import Project
from django.shortcuts import render, redirect
from .forms import ContactForm
def home(request):
    projects = [
        {"title": "Project 1", "description": "Description of Project 1", "image": None, "link": "#", "technologies_used": "Python, Django"},
        {"title": "Project 2", "description": "Description of Project 2", "image": None, "link": "#", "technologies_used": "JavaScript, React"},
        # Add more project data here
    ]
    return render(request, 'myportfolio/home.html', {'projects': projects})

def cv(request):
    return render(request, 'myportfolio/cv.html')

def contact(request):
    return render(request, 'myportfolio/contact.html')

