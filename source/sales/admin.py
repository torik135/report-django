from django.contrib import admin
from .models import Position, Sale, CSV

class PositionAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price', 'created')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'total_price', 'customer', 'salesman', 'created', 'updated')

class CSVAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'created', 'updated')

admin.site.register(Position, PositionAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(CSV, CSVAdmin)