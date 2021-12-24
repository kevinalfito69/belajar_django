from django.db import models

# Create your models here.

class instagram(models.Model):
    nama_depan = models.CharField(("Nama Depan"), max_length=50)
    nama_belakang = models.CharField(("Nama Belakang"), max_length=50)
    username = models.CharField(("Username"), max_length=50)

    def __str__(self) :
        return "{}. {}".format(self.id,self.username)
