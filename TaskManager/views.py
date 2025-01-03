from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        account_type = request.POST.get('account_type')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if account_type == 'staff':
                if not user.is_staff:
                    return HttpResponse("Acceso denegado : no cuenta con permisos para iniciar sesion como admin", status=403)
                else:
                    return redirect(reverse('admin:index'))
            elif account_type == 'non_staff':
                if user.is_staff:
                    return HttpResponse("Debe iniciar sesion como admin", status=403)
                return redirect('index')               
        else:
            return HttpResponse("Usuario no encontrado", status=403)

    return render(request, 'admin/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            
            group, created = Group.objects.get_or_create(name='RegUsers')
            user.groups.add(group)  # Add the user to the RegUsers group
            
            messages.success(request, 'User registered successfully and added to RegUsers group!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})