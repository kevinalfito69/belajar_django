from django.shortcuts import render,redirect
from .models import PostModel
from .forms import PostForm
# Create your views here.

def index(request):
    postmodel = PostModel.objects.all()
    context ={
        'title':'data pendaftar',
        'postmodel':postmodel
    }
    return render(request,'daftar/index.html',context)

def daftar(request):
    postform = PostForm(request.POST or None)
    if request.method == 'POST':
        if postform.is_valid():
            postform.save()
            return redirect('daftar:index')
    context = {
    'title' : 'pendaftaran',
    'postform' : postform
    }
    return render(request,'daftar/daftar.html',context)