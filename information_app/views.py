from django.shortcuts import render, redirect
from .forms import CreateProductForm
from django.db import connection


def exec_sp():
    with connection.cursor() as cursor:
        # cursor.callproc('SP_pruebaDjango')
        cursor.execute('SP_pruebaDjango')


def create_product(request):
    template_name = "information_app/create_product.html"
    if request.method == "GET":
        form = CreateProductForm()
    
    else:
        form = CreateProductForm(request.POST)
        if form.is_valid():
            exec_sp()
            form.save()

        return redirect("index")
    return render(request, template_name, {"form": form})