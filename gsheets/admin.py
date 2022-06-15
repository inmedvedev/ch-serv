from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'number',
        'dollar_cost',
        'ruble_cost',
        'delivery_time'
    ]
    list_display = [
        'id',
        'number',
        'dollar_cost',
        'ruble_cost',
        'delivery_time'
    ]
