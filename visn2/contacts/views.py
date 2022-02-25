from django.shortcuts import render

def contactsView(request):
    context = {}
    return render(request, 'contacts.html', context)
