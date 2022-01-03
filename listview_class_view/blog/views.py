
# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
# model
from .models import Artikel
class Artikel(ListView):
    model = Artikel
    ordering = ['update']
    paginate_by = 2
    extra_context = {
         'title' : 'list',
    }
   
    def get_queryset(self):
        if self.kwargs['penulis'] != 'all':
            self.queryset = self.model.objects.filter(penulis__iexact = self.kwargs['penulis'])
            self.kwargs.update({
                'penulis' : self.kwargs['penulis'],
            })
        return super().get_queryset()
    
    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
def index(request):
    context={
        'title' : 'list',

    }
    return render(request,'blog/index.html',context)
