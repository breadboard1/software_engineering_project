from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from cars.models import Car
from .models import Buy

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully.')
            return redirect('signin')
    else:
        register_form = forms.RegistrationForm()
    return render(request, './users/sign_up.html', {'form': register_form, 'type':'Signup'})

class UserLogInView(LoginView):
    template_name = './users/sign_in.html'
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successful.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Invalid Username Or Password.')
        return super().form_invalid(form)

class UserLogOutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('signin')

@login_required
def profile(request):
    return render(request, './users/profile.html')

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
    return render(request, './users/update_profile.html', {'form':profile_form})

@login_required
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
    return render(request, './users/change_password.html', {'form':form})

@login_required
def buy_now(request, id):
    car = get_object_or_404(Car, id=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
    else:
        messages.info(request, 'You can not buy it now')
        return redirect('profile')
    Buy.objects.create(user=request.user, car=car)
    return redirect('profile')

class ProfileView(TemplateView):
    template_name = './users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buys'] = Buy.objects.filter(user=self.request.user)
        return context