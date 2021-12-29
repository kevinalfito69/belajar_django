from django.urls import path

from . import views
from .views import(
 SosmedListView,
 DeleteView,
 SosmedFormView,

 )
app_name = 'sosmed'

urlpatterns = [
	path('delete/<int:delete_id>/', DeleteView.as_view(), name='delete'),
	path('update/<int:update_id>/', SosmedFormView.as_view(mode='update'), name='update'),
	path('create/',SosmedFormView.as_view(mode='create'), name='create'),
	path('',SosmedListView.as_view(), name='list'),
]