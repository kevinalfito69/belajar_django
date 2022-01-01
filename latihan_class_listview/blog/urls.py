from django.urls import path
from .views import BiodataViews
urlpatterns = [
    path('',BiodataViews.as_view(), name='list')
]

