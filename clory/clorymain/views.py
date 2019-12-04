from django.shortcuts import render
from django.views.generic import ListView
from clory_data.models import Product

def home(request):
    return render(request, 'home.html')


class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_queryset(self):
        return Product.objects.all()
