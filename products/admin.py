from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    #This shows all the columns of a product listed here
    list_display = ('name', 'price', 'category', 'is_available', 'average_rating', 'food_type')

    #This adds a sidebar and shows all the ways you can filter the products
    list_filter = ('category', 'food_type', 'is_available')

    #This allows you to search for products based on name, food type and is available or not
    search_fields = ('name',)

    #This organizes form into different sections (same like in HTML fieldset)
    fieldsets = (
        ('Product Details', {
            'fields': ('name','price', 'category', 'food_type')
        }),
        ('Status', {
            'fields': ('is_available',)
        }),
        ('Product Image', {
            'fields': ('image',)
        }),
    )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Product, ProductAdmin)
