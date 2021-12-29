from django.db import models

# Create your models here.
class ModelBiodata(models.Model):
    nama_depan = models.CharField(("Nama Depan"), max_length=50)
    nama_belakang = models.CharField(("Nama Belakang"), max_length=50)
    kelamin = (
        ('Laki-Laki','laki-laki'),
        ('Perempuan','perempuan')
    )
    jenis_kelamin = models.CharField(max_length=100,choices=kelamin)
    def __str__(self):
        return "{}.{} {}".format(self.id,self.nama_depan,self.nama_belakang)