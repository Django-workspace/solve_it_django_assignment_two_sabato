from dataclasses import fields
import imp
from pyexpat import model
from django import forms
from .models import Trainee

class TraineeForm(forms.ModelForm):
    class Meta:
        model=Trainee
        fields= ['full_name','dob']
        