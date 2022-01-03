from django.urls import path

from .models import Artikel

from .views import index
from .views import Artikel
app_name = 'blog'
urlpatterns = [
    path('<str:penulis>/<int:page>',Artikel.as_view(),name='list'),
    

]
