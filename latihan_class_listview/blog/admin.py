from django.contrib import admin
from .models import Biodata

# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
        'update'
        ]
admin.site.register(Biodata,BiodataAdmin)