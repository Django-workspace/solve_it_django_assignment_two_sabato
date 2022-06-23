from unicodedata import name
from django.urls import path,URLPattern
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("trainee/delete/<str:trainee_id>/",views.delete,name="delete"),
    # path("trainee/edit/<str:trainee_id>/",views.edit,name="edit")

]