from django.db import models
from django.forms.widgets import Widget

# Create your models here.
class PostModel(models.Model):
    jeniskelamin = (
        ('Laki-Laki','laki-laki'),
        ('Perempuan','perempuan'),
    )
    nama = models.CharField(max_length=40)
    jenis_kelamin = models.CharField(max_length=40, choices=jeniskelamin)
    alamat = models.TextField()
    tanggal_lahir = models.DateField()


