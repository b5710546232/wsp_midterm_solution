from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, 'login/index.html')


def register_view(request):
    return render(request, 'login/register.html')


def success(request):
    print(request.user)
    user = request.user
    return HttpResponse("Welcome %s" % user.username)


def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
    user.save()
    return HttpResponseRedirect(reverse('login:index'))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('login:success'))
    else:
        return HttpResponseRedirect(reverse('login:index'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login:index'))
