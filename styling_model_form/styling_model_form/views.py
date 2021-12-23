from django.shortcuts import render
def index(request):
    context = {
        'title':'index',
        'content':'ini adalah index',
    }
    return render(request,'index.html',context)