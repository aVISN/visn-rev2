import os
from visn2 import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, FileResponse
from .models import *
from dashboard.forms import *


def filesView(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login'))
    search_text = request.GET.get('search_text')
    if search_text:
        files = ProjFile.objects.filter(author=request.user).filter(filename__contains=search_text).all()
    else:
        files = ProjFile.objects.filter(author=request.user).all()

    print(files)
    context['files'] = files

    users = User.objects.all()
    chat_form = MessageForm()
    context['target_users'] = users
    context['chat_form'] = chat_form
    if request.method == 'POST':
        f = MessageForm(request.POST)
        if f.is_valid():
            to_name = f.cleaned_data.get('mto')
            mto = User.objects.filter(username=to_name).first()
            Message(mfrom=request.user, msg=f.cleaned_data.get('message'), mto=mto).save()

    return render(request, 'files/files.html', context)


def newFile(request):
    context = {}
    users = User.objects.all()
    chat_form = MessageForm()
    context['target_users'] = users
    context['chat_form'] = chat_form
    if request.method == 'POST':
        f = MessageForm(request.POST)
        if f.is_valid():
            to_name = f.cleaned_data.get('mto')
            mto = User.objects.filter(username=to_name).first()
            Message(mfrom=request.user, msg=f.cleaned_data.get('message'), mto=mto).save()

    form = ProjFileForm(request.POST, request.FILES)
    if form.is_valid():
        print('bbb...')
        print(form.cleaned_data)
        p = ProjFile(project=form.cleaned_data.get('project'), 
            filename=form.cleaned_data.get('filename'),
            comment=form.cleaned_data.get('comment'),
            author=request.user)
        p.save()
        return redirect(reverse_lazy('files'))
    else:
        print('aaa....')
        for err in form.errors:
            print(err)

    form = ProjFileForm()
    context['form'] = form
    return render(request, 'files/new_file.html', context)


def file_response_download1(request, filepath):
    filepath = os.path.join(settings.MEDIA_ROOT, filepath)
    print(filepath)
    response = FileResponse(open(filepath, 'rb'))
    response['content_type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment; filename=' + os.path.split(filepath)[-1]
    return response