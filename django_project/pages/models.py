from django.db import models

# Create your models here.
from django.db import db

class MenuResto(models.Model):
    KATEGORI_CHOICES = [
        ('MAKANAN', 'Makanan'),
        ('MINUMAN', 'Minuman'),
        ('SNACK', 'Cemilan'),
    ]

    nama = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    harga = models.DecimalField(max_digits=10, decimal_places=0) # Contoh: 25000
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES, default='MAKANAN')
    tersedia = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nama} - Rp {self.harga}"