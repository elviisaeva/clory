from django.shortcuts import render
from django.views.generic import ListView
from clory_data.models import Product

def home(request):
    return render(request, 'home.html')

def zara(request):
    return render(request, 'zara.html')

def zara_women(request):
    return render(request, 'zara_women.html')

def zara_all(request):
    return render(request, 'zara_all.html') 

def zara_dress(request):
    return render(request, 'zara_dress.html')

def zara_tshirt(request):
    return render(request, 'zara_tshirt.html')

def zara_trouser(request):
    return render(request, 'zara_trouser.html')

class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_queryset(self):
        return Product.objects.all()
