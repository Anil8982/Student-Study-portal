from django import forms
from .models import Homework,Notes 
from django.forms import widgets
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']  

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model=Homework
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']

class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search:")
    
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        widgets = {'due': DateInput()}
        fields = [ 'title', 'is_finished']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']