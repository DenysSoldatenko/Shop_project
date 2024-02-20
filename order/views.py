from django.shortcuts import render

# Create your views here.
def create_order(request):
    return render(request, 'order/create_order.html')