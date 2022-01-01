from django.shortcuts import render
from django.views.generic import ListView
from .models import Biodata

# Create your views here.
class BiodataViews(ListView):
    model = Biodata
    extra_context = {
        'title':'list data'

    }
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
