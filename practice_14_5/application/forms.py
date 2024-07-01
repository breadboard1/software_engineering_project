from .models import ExampleModel
from django import forms

class ExampleModelForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = '__all__'
        widgets = {
            'email' : forms.EmailInput(attrs={'placeholder':'Enter Your Email'}),
            'name' : forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
        }