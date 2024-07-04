from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        resister_form = forms.ResistrationForm(request.POST)
        if resister_form.is_valid():
            resister_form.save()
            messages.success(request, 'Account Created Successfully.')
            return redirect('login')
    else:
        resister_form = forms.ResistrationForm()
    return render(request, './authors/sign_up.html', {'forms': resister_form, 'type':'Signup'})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_password)
            if user is not None:
                messages.success(request, 'Logged in Successfully.')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Invalid Username or Password')
                return redirect('log_in')
    else:
        form = AuthenticationForm()
    return render(request, './authors/sign_up.html', {'forms':form, 'type':'Login'})

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, './authors/profile.html', {'data':data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.Update(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Updated Profile Successfully.')
            return redirect('profile')
    else:
        profile_form = forms.Update(instance = request.user)
    return render(request, './authors/update_profile.html', {'form':profile_form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Updated Successfully.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, './authors/change_pass.html', {'form':form})

def log_out(request):
    logout(request)
    return redirect('login')