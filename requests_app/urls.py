from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/lisafile/', views.LisaFile.as_view(), name="create_lisafile"),
    path('create/cenfile/', views.CenFile.as_view(), name="create_cenfile"),
]