from django.shortcuts import render, redirect
from .forms import RegisterForm, Update
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def home(request):
    return render(request, './home.html')

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, './application/sign_up.html', {'form': form})
    else:
        return redirect('profile')

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userPass = form.cleaned_data['password']
                user = authenticate(username=name, password=userPass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Welcome back!')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './application/log_in.html', {'form': form})
    else:
        return redirect('profile')

def profile(request):
    # if request.user.is_authenticated:
    #     return render(request, './application/profile.html', {'user': request.user})
    # return redirect('login')
    return update_profile(request)

def log_out(request):
    logout(request)
    return redirect('login')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, './application/pass_change.html', {'form':form})
    else:
        return redirect('login')

def change_pass_without_old_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, './application/pass_change.html', {'form':form})
    else:
        return redirect('login')

def update_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Update(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Updated successfully')
                return redirect('profile')
        else:
            form = Update(instance=request.user)
        return render(request, './application/profile.html', {'form': form})
    else:
        return redirect('login')
