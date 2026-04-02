from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MenuResto

@admin.register(MenuResto)
class MenuRestoAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kategori', 'harga', 'tersedia')
    list_filter = ('kategori', 'tersedia')
    search_fields = ('nama',)
    