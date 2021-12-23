from django.db import models

# Create your models here.
class PostModel(models.Model):
    judul = models.CharField(("Judul"), max_length=50)
    body = models.TextField(("Body Postingan"))
    author = models.CharField(("Author"), max_length=50)
    ListCategory=(
        ('Jurnal','jurnal'),
        ('Berita','berita'),
        ('Gosip','gosip')

    )
    category = models.CharField(("Category"),choices=ListCategory, max_length=50)
    def __str__(self):
        return "{}.{}".format(self.id,self.judul)

