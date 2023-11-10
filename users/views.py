from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company

# register applicant only

def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been successfully created.')
            return redirect('login')
        else:
            messages.warning(request, 'Something actually went wrong!')
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_applicant.html', context)
    

# register recruiter only

def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your company has been successfully created.')
            return redirect('login')
        else:
            messages.warning(request, 'Something actually went wrong!')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_recruiter.html', context)
    

# login a user
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if request.user.is_applicant:
                return redirect('applicant-dashboard')
            elif request.user.is_recruiter:
                return redirect('recruiter-dashboard')
            else:
                return redirect('login')
        else:
            messages.warning(request, 'Something actually went wrong!')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    

# logout a user
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')