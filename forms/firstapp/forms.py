from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="Username", help_text="length must be in 70 characters", required=False, widget=forms.Textarea(attrs={'id':'text_area', 'placeholder':'Enter your name...'}))
    file = forms.FileField()
    email = forms.EmailField()
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField(required=False)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    ITEAMS = [('B', 'Beef'), ('M', 'Mashroom'), ('C', 'Chicken')]
    pizza = forms.MultipleChoiceField(choices=ITEAMS, widget=forms.CheckboxSelectMultiple)

class studentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    age = forms.IntegerField()
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")
    #     return valemail
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com")