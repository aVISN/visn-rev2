from django.shortcuts import render

def filesView(request):
    context = {}
    return render(request, 'files/files.html', context)
