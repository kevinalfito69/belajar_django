from django import forms
from django.forms import widgets 
from .models import ModelBiodata

class FormBiodata(forms.ModelForm):
    
    class Meta:
        model = ModelBiodata
        fields = [
            "nama_depan",
            "nama_belakang",
            "jenis_kelamin",
            
            ]
        widgets = {
           'jenis_kelamin': forms.Select()
        }
