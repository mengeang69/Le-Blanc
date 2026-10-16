from django.shortcuts import render, get_object_or_404
from .models import Perfume

def home(request):
    perfumes = Perfume.objects.filter(in_stock=True)
    return render(request, 'index.html', {'perfumes': perfumes})

def product_detail(request, pk):
    perfume = get_object_or_404(Perfume, pk=pk)
    return render(request, 'product.html', {'perfume': perfume})

def about(request):
    return render(request, 'about.html')