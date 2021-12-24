from django.urls import path, re_path
from . import views
app_name = 'sosmed'
urlpatterns = [
    path('',views.list,name='list'),
    re_path('delete/(?P<delete_id>[0-9]+)',views.delete,name='delete'),
    
    path('create/',views.create,name='create')
]
