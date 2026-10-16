from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Perfume

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'in_stock')
    list_filter = ('brand', 'in_stock')
    search_fields = ('name', 'brand')