from django import forms
from django.forms import fields 
from .models import instagram
class InstagramForms(forms.ModelForm):
    class Meta:
        model = instagram
        fields = [
            'nama_depan',
            'nama_belakang',
            'username',
        ]
    Meta