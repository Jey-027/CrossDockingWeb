from django.contrib import admin
from .models import OrderDetail, OrderHeader, Order

admin.site.register(OrderDetail)
admin.site.register(OrderHeader)
admin.site.register(Order)