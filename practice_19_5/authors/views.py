from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def sign_up(request):
    if request.method == 'POST':
        resister_form = forms.ResistrationForm(request.POST)
        if resister_form.is_valid():
            resister_form.save()
            return redirect('login')
    else:
        resister_form = forms.ResistrationForm()
    return render(request, './authors/sign_up.html', {'form': resister_form, 'type':'Signup'})

class UserLoginView(LoginView):
    template_name = './authors/sign_in.html'
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class UserLogOutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('login')

@login_required
def profile(request):
    data = request.user
    return render(request, './authors/profile.html', {'data':data})
