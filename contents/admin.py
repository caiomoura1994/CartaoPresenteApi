from django.contrib import admin

from .models import Product, Image, Order


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


class OrderInline(admin.StackedInline):
    model = Order.product.through
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    exclude = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
