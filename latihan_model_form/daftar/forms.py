from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):

    
    class Meta:
        model = PostModel
        fields = (
            'nama',
            'jenis_kelamin',
            'alamat',
            'tanggal_lahir',

        )
