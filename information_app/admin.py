from django.contrib import admin
from .models import OrderStatus, UserPrinter, Product, Store, parameters


admin.site.register(OrderStatus)
admin.site.register(UserPrinter)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(parameters)

