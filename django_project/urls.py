from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Fungsi sederhana langsung di dalam file URL
def tes_halo(request):
    return HttpResponse("<h1>Selamat Pak Joko! Project Django Berhasil Jalan.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tes_halo), # Ini akan muncul di halaman utama 127.0.0.1:8000
]