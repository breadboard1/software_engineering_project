from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
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
    return render(request, './authors/sign_up.html', {'form': resister_form, 'type':'Signup'})

class UserLoginView(LoginView):
    template_name = './authors/sign_up.html'
    def get_success_url(self) -> str:
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successful.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Invalid Username Or Password.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

class UserLogOutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('login')

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