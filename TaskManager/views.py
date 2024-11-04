from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'User registered successfully!')
            return HttpResponse("User added succesfully")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})