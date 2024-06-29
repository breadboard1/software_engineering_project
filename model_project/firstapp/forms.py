from django import forms
from . models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student roll'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'btn-primary'}),
            'roll' : forms.NumberInput(),
        }
        help_texts = {
            'name' : 'Write your full name',
        }
        error_messages = {
            'name' : {'required':'Your name is required'},
        }
