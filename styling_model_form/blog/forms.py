from django import forms
from django.forms.widgets import Textarea
from .models import PostModel

class PostForm(forms.ModelForm):
    
    class Meta:
        
        model = PostModel
        fields = [
            'author',
            'judul',
            'body',
            'category'
        ]
        widgets = {
            'judul' : forms.TextInput(
               attrs={
               'class':'form-control',
               'placeholder':'Judul artikel'
                    }
                 
            ),
            'author': forms.TextInput(
              attrs={
               'class':'form-control',
               'placeholder':'Nama Penulis'
                    }
            ),
            'body': forms.Textarea(
              attrs={
               'class':'form-control',
               
                    }
            ),
            'category': forms.Select(
              attrs={
               'class':'form-control',
               
                    }
            ),
        }
