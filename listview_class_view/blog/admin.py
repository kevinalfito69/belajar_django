from django.contrib import admin
from .models import Artikel
# Register your models here.

class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
        'update',
        
    ]
admin.site.register(Artikel,ArtikelAdmin)