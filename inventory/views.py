from django.shortcuts import render

def catalog(request):
    return render(request, 'inventory/catalog.html')


def product(request):
    return render(request, 'inventory/product.html')
