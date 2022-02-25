from django.shortcuts import render

def chatView(request):
    context = {}
    return render(request, 'chat/chat.html', context)
