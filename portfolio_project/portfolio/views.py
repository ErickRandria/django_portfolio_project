from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
