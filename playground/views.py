from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from .forms import CustomUserCreationForm
from playground.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Create your views here.
def say_hello(request):
    return render(request,'home.html')

def page2(request):
    return render(request,'page2.html')

def register_view(request):
    if request.method == 'POST':
        # Fetch data from the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

            # Validate and save the data
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
        else:
            # Save user to the database
            user = User(full_name=full_name, email=email, password=password)
            user.save()
            messages.success(request, "User registered successfully!")
            return render(request,'login.html')  # Replace 'success_page' with your success URL

    # Render the registration form
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Fetch the user by email
            user = User.objects.get(email=email)

            # Check if the provided password matches the stored hashed password
            if check_password(password, user.password):
                # Password is correct, log the user in
                request.session['user_id'] = user.id  # Store user ID in session or use Django's session mechanism
                messages.success(request, "Login successful!")
                return render(request,'home.html')  # Redirect to home page or another page after login
            else:
                messages.error(request, "Invalid password! Please try again.")
        except User.DoesNotExist:
            messages.error(request, "User not found! Please register first.")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home or another page after logout



