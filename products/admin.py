from django.contrib import admin
from .models import Product, Category, PreRelease

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'is_exclusive',
        'pre_release',
        'age',
        'image'
    )

    ordering = ('sku',)


class PreReleaseAdmin(admin.ModelAdmin):
    list_display = (
        'pre_release',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PreRelease, PreReleaseAdmin)
