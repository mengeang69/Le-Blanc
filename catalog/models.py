from django.db import models

# Create your models here.
from django.db import models

class Perfume(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    scent_family = models.CharField(max_length=150)
    description = models.TextField()
    top_notes = models.CharField(max_length=200)
    base_notes = models.CharField(max_length=200)
    longevity = models.CharField(max_length=50)
    image = models.ImageField(upload_to='perfumes/')
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} - {self.name}"