from django.shortcuts import render, redirect
from .forms import productForm
from .models import products




def product_list(request):
    context = {'product_list': products.objects.all()}
    return render(request, "productapp/list.html", context)


def product_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = productForm()
        else:
            product = products.objects.get(pk=id)
            form = productForm(instance=product)
        return render(request, "productapp/form.html", {'form': form})
    else:
        if id == 0:
            form = productForm(request.POST)
        else:
            product = products.objects.get(pk=id)
            form = productForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/list')


def product_delete(request, id):
    product = products.objects.get(pk=id)
    product.delete()
    return redirect('/list')






# Create your views here.
