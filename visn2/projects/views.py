from django.shortcuts import render

def projectsView(request):
    context = {}
    return render(request, 'projects/projects.html', context)

def singleProjectView(request):
    context = {}
    return render(request, 'projects/project.html', context)
