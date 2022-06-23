from cProfile import label
from dataclasses import fields
import imp
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Trainee
import datetime
from .widgets import DatePickerInput
class TraineeForm(forms.ModelForm):
    dob=forms.DateField(label="date of birth",initial=datetime.date.today)
    full_name = forms.CharField(label="your full name")
    class Meta:
        model=Trainee
        fields= ['full_name','dob']
        
        widgets = {
            'dob':DatePickerInput()
        }