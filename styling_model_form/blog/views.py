from django.shortcuts import render, redirect
from .forms import PostForm
from .models import PostModel

# Create your views here.
def list(request):
    postmodel=PostModel.objects.all()
    context = {
        'title':'ini adalah list post',
        'postmodel' : postmodel,
    }
    return render(request, "blog/list.html", context)
def create(request):
    postform = PostForm(request.POST or None)
    if request.method == 'POST': #POST REQUEST BROWSER
        if postform.is_valid() :
            postform.save()
            return redirect('blog:list')
    context = {
        'title':'Input Postingan',
        'postform' : postform,
    }
    return render(request,'blog/create.html', context)



