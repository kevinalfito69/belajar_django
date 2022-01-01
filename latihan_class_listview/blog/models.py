from abc import update_abstractmethods
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Biodata(models.Model):
    nama            = models.CharField(max_length=255)
    umur            = models.CharField(max_length=4)
    tanggal_lahir   = models.DateField()
    publish         = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)
    slug            = models.SlugField()
    def save(self):
          self.slug = slugify(self.nama)
          super(Biodata, self).save()
    def __str__(self):
        return "{}. {}".format(self.id, self.nama)