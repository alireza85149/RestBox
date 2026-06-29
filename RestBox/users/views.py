from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile
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
    error = None
    if request.method == 'POST':
        if role == 'host':
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if len(password) < 8:
                error = "error: The password must be at least eight characters."
                return render('users/registeration.html', {'error': error, 'role': role})
            try:
                hashed_password = make_password(password)
                user = UserProfile.objects.create(
                    fullname=fullname,
                    email=email,
                    password=hashed_password,
                    role=role
                )
                return redirect(reverse('users:user_login', kwargs={'role':role}))

            except:
                error = 'this accountwith this email is already exists.'
                return render(request , 'users/registeration.html', {'error': error, 'role': role})

        elif role == 'guest':
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if len(password) < 8:
                error = "error: The password must be at least eight characters."
                return render(request, 'users/registeration.html', {'error': error, 'role': role})
            try:
                hashed_password = make_password(password)
                user = UserProfile.objects.create(
                    fullname=fullname,
                    email=email,
                    password=hashed_password,
                    role=role
                )
                return redirect(reverse('users:user_login', kwargs={'role':role}))
            except:
                error = 'this accountwith this email is already exists.'
                return render(request , 'users/registeration.html', {'error': error , 'role': role})
        
    return render(request, 'users/registeration.html')
    
def login(request, role):
    error = None
    if role == 'host':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserProfile.objects.get(email=email, role=role)
            if check_password(password, user.password):
                return redirect('users:index')
            else:
                error = "error: The password is wrong"
        except UserProfile.DoesNotExist:
            error = "No user with these specifications was found."
            
        return render(request, 'users/login.html', {'error': error, 'role' : role})
            
    elif role == 'guest':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserProfile.objects.get(email=email, role=role)
            if check_password(password, user.password):
                return redirect('user:index')
            else:
                error = "error: The password is wrong"
        except:
            error = "error: No user with these specifications was found."
        
        return render(request, 'users/login.html', {'error': error, 'role': role})
    
    return render(request, 'users/login.html')
