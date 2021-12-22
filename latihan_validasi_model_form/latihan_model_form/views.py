from django.shortcuts import render
def index(request):
    context={
        'title': 'index'
    }
    return render(request,'index.html',context)