from . import views
from django.urls import path
app_name = 'biodata'

urlpatterns = [
    path("",views.list,name="list"),
    path("create/",views.create,name="create"),
    path("delete/<int:delete_id>/", views.delete, name="delete"),
    path("edit/<int:edit_id>/", views.edit, name="edit"),
]
