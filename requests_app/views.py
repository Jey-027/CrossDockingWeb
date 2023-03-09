from django.shortcuts import render
from .models import LisaFile, CenFile
from django.views.generic.edit import CreateView


def index(request):
    return render(request, 'index.html', {})


class LisaFile(CreateView):
    model = LisaFile
    fields = "__all__"
    template_name = "solicitudes_app/create_lisafile.html"
    success_url = ""


class CenFile(CreateView):
    model = CenFile
    fields = "__all__"
    template_name = "solicitudes_app/create_cenfile.html"
    success_url = ""
