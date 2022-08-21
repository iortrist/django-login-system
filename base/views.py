from email import message
import imp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from loginsystem import settings
from django.core.mail import send_mail
# Create your views here.


def userRegister(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exists.")
            return redirect('register')

        if password1 != password2:
            messages.error(
                request, "Password did not match.")
            return redirect('register')

        if password1 == password2 and len(password1) < 8:
            messages.error(
                request, "Password must be at least 8 characters long.")
            return redirect('register')

        if not username.isalnum():
            messages.error(
                request, "Username must be alpha-numeric only.")
            return redirect('register')

        if len(username) < 4:
            messages.error(
                request, "Username must be at least 4 characters long.")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(
                request, "Email already exists.")
            return redirect('register')

        user = User.objects.create_user(username, email, password1)
        user.save()

        messages.success(
            request, "Your account has been created successfully! Please check your email to confirm registration. ")

        subject = "Welcome to Django Login Practice"
        message = f"Hello {user.username}! Thank you for registering!"
        sender = settings.EMAIL_HOST_USER
        recipient = [user.email]
        send_mail(subject, message, sender, recipient, fail_silently=True)

        return redirect('login')

    return render(request, 'base/register.html')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(
                request, "Invalid username/password. Please try again.")
            return redirect('login')
    return render(request, 'base/login.html')


def userLogout(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'base/home.html')
