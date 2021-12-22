from django.urls import path
from . import views
app_name = 'daftar'
urlpatterns = [
    path('',views.index,name='index'),
    path('daftar/',views.daftar,name='daftar')
]
