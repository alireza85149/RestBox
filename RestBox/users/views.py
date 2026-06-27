from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def role_handling(request):
    role = request.POST.get('role')
    action= request.POST.get('action')

    if action == 'register':
        return redirect(reverse('users:registeration' , kwargs={'role':role}))
    elif action == 'login':
        return redirect(reverse('users:user_login' , kwargs={'role':role}))
# the below functions are just sturctures and they should be compeleted later
def registeration(request, role):
    if role == 'host':
        # return HttpResponse('this is registeration page for hosts')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return render(request, 'users/registeration.html')
    elif role == 'guest':
        # return HttpResponse('this is registeration page for guest')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return render(request, 'users/registeration.html')
    
def login(request, role):
    if role == 'host':
        # return HttpResponse('this is login page for hosts')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return render(request, 'users/login.html')
    elif role == 'guest':
        # return HttpResponse('this is login page for guest')
        email = request.POST.get('email')
        password = request.POST.get('password')
        return render(request, 'users/registeration.html')