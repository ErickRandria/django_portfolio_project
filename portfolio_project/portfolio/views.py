from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request, 'portfolio/home.html')

def home(request):
    projects_show = [
        {
            'title':'Project 1',
            'path': 'images/projects_img/project1.png',
        },
        {
            'title':'Project 2',
            'path': 'images/projects_img/project2.png',
        },
        {
            'title':'Project 3',
            'path': 'images/projects_img/project3.png',
        },
        {
            'title':'Project 4',
            'path': 'images/projects_img/project4.png',
        },
        {
            'title':'Project 5',
            'path': 'images/projects_img/project5.png',
        },
        {
            'title':'Project 6',
            'path': 'images/projects_img/project6.png',
        },
    ]
    return render(request, 'portfolio/home.html',{'projects_show': projects_show})