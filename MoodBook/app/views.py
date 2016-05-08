"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth import login, authenticate
from .models import *
from .forms import RegisterForm
from django.contrib.auth.models import User, Group
from django.db import transaction

@transaction.atomic
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            user = form.save()
            default_group = Group.objects.get(name="user")
            user.groups.add(default_group)
            user.save()

            user = authenticate(username = user.username, password = password)
            login(request, user)
            return HttpResponseRedirect('user/diary')

    if request.user.is_authenticated():
        return redirect('user/diary')
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'form': RegisterForm,
        })
    )

@login_required
@transaction.atomic
def diary(request):
    assert isinstance(request, HttpRequest)
    #user = User.objects.get(pk = request.user.pk)
    group = request.user.groups.all()[0]
    if group.name == 'user':
        records = Record.objects.filter(user__username=request.user.username)
        return render(request,
                      'app/user.html',
                      context_instance= RequestContext(request,
                      {
                          'records': records,
                          'title': 'MBStorage',
                          'year': datetime.now().year
                      }))
    else:
        user_ids = DoctorUsers.objects.filter(doctor_id=request.user.id)
        users = []
        for u in user_ids:
            user = User.objects.get(pk = u.user_id)
            users.append(user)

        return render(request,
                      'app/doctor.html',
                      context_instance = RequestContext(request,
                      {
                          'year': datetime.now().year,
                          'title': "Doctor's page",
                          'users': users
                      }))


#angry - 0
#sad - 1
#surprised - 2
#happy - 3
@login_required
def detection(request):
    """Renders the detection page"""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        body_unicode = str(request.body.decode('utf-8'))
        data = list(body_unicode.split('&'))
        emotions = []
        for d in data:
            emotion = d.split('=')
            emotions.append(emotion[1])

    return render(
        request,
        'app/realtime.html',
        context_instance = RequestContext(request,
        {
            'title':'MBDetection',
            'year': datetime.now().year
        })
    )

def newrecord(request):
    """Renders the record creation page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newrecord.html',
        context_instance = RequestContext(request,
        {
            'title' : 'NewRecord',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
