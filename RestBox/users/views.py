from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile
from django.db import IntegrityError
# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def role_handling(request):
    role = request.POST.get('role')
    action = request.POST.get('action')

    if action == 'register':
        return redirect(reverse('users:registeration', kwargs={'role': role}))
    elif action == 'login':
        return redirect(reverse('users:user_login', kwargs={'role': role}))

def registeration(request, role):
    error = None
    if request.method == 'POST':
        if role == 'host':
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
                return redirect(reverse('users:user_login', kwargs={'role': role}))

            except IntegrityError:
                error = 'this accountwith this email is already exists.'
                return render(request, 'users/registeration.html', {'error': error, 'role': role, 'email': email})

        elif role == 'guest':
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if len(password) < 8:
                error = "error: The password must be at least eight characters."
                return render(request, 'users/registeration.html', {'error': error, 'role': role, 'email': email})
            try:
                hashed_password = make_password(password)
                user = UserProfile.objects.create(
                    fullname=fullname,
                    email=email,
                    password=hashed_password,
                    role=role
                )
                return redirect(reverse('users:user_login', kwargs={'role': role}))
            except IntegrityError:
                error = 'this accountwith this email is already exists.'
                return render(request, 'users/registeration.html', {'error': error, 'role': role})
        
    return render(request, 'users/registeration.html')
    
def login(request, role):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'role': role})
    
    elif request.method == 'POST':
        error = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            error = "Please enter both email and password"
            return render(request, 'users/login.html', {
                'error': error,
                'role': role
            })
        
        try:
            user_profile = UserProfile.objects.get(email=email, role=role)
            
            if check_password(password, user_profile.password):
                if role == 'host':
                    return redirect('users:host_dashboard')
                else:
                    return redirect('users:index')  
            else:
                error = "The password is incorrect"
                
        except UserProfile.DoesNotExist:
            error = "No user found with these credentials"
        
        return render(request, 'users/login.html', {
            'error': error,
            'role': role
        })
    
    return render(request, 'users/login.html', {'role': role})

def host_dashboard(request):
    return render(request, 'users/host_dashboard.html')