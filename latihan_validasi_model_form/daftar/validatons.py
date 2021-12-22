from django.core.exceptions import ValidationError
def validate_nama(value):
    nama_post = 'dimas'
    if value == nama_post :
        raise ValidationError("Tidak boleh menggunakan nama tersebut")