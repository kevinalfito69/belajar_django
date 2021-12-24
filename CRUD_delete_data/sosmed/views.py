from django.db import models
from django.shortcuts import render, redirect
from .models import instagram
from .forms import InstagramForms

# Create your views here.
def delete(request,delete_id):
    instagram.objects.filter(id=delete_id).delete()
    return redirect('sosmed:list')


def list(request):
    akun = instagram.objects.all()
    context = {
        'title':'Sosmed',
        'akun' : akun
    }
    return render(request,'sosmed/list.html',context)
def create(request):
    instagramforms=InstagramForms(request.POST or None)
    if request.method == 'POST':
        if instagramforms.is_valid():
            instagramforms.save()
            return redirect('sosmed:list')
    context = {
        'title':'Create data',
        'instagramforms' : instagramforms
    }
    return render(request,'sosmed/create.html', context)
