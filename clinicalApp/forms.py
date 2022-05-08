from dataclasses import fields
from clinicalApp import models
from django import forms

from .models import clinicalData, patient

class patientForm(forms.ModelForm):
    class Meta:
        model=patient
        fields='__all__'

class clinacalDataFrom(forms.ModelForm):
    class Meta:
        model=clinicalData
        fields='__all__'