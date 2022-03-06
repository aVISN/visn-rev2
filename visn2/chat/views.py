from django.shortcuts import render, redirect
from .models import *
from dashboard.forms import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def chatView(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login'))
    context = {}
    if request.method == 'POST':
        f = MessageForm(request.POST)
        print('aaa')
        if f.is_valid():
            print('save')
            to_name = f.cleaned_data.get('mto')
            mto = User.objects.filter(username=to_name).first()
            Message(mfrom=request.user, msg=f.cleaned_data.get('message'), mto=mto).save()

    search_text = ''
    if request.method == 'GET':
        search_text = request.GET.get('search_text')
    if search_text:
        search_text = search_text.strip()
    talks = Message.objects.filter(Q(mto=request.user) | Q(mfrom=request.user)).order_by('-msgTime')
    if search_text:
        last_msgs = Message.objects.filter(Q(mto=request.user) | Q(mfrom=request.user)).filter(msg__icontains=search_text).order_by('-msgTime')[:10]
    else:
        last_msgs = talks[:10]

    talkers = set()
    for talk in talks:
        if len(talkers) >= 5:
            break
        if talk.mto == request.user:
            talkers.add(talk.mfrom)
        else:
            talkers.add(talk.mto)
    
    last_talks = []
    for talker in talkers:
        last_talks.append([talker, Message.objects.filter(Q(mto=talker, mfrom=request.user) | Q(mto=request.user, mfrom=talker)).order_by('-msgTime')[:10]])
    form = MessageForm()
    context['last_msgs'] = last_msgs
    context['chat_form'] = form
    context['last_talks'] = last_talks
    context['target_users'] = User.objects.all()
    return render(request, 'chat/chat.html', context)
