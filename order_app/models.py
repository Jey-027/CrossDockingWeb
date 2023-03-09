from django.db import models
from information_app.models import UserPrinter, OrderStatus

class OrderDetail(models.Model):
    order_number = models.IntegerField(primary_key=True)
    lisa_number = models.IntegerField()
    picking_number = models.IntegerField()
    ean_store = models.CharField(max_length=15)
    ean_sku = models.CharField(max_length=15)
    sku = models.CharField(max_length=30)
    quantity_to_collect = models.IntegerField()
    quantity_inventoried = models.IntegerField()
    user_terminal = models.ForeignKey(UserPrinter, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order_number}"
    

class OrderHeader(models.Model):
    order_number = models.IntegerField(primary_key=True)
    lisa_number = models.IntegerField()
    expiration_date = models.DateField()
    approved = models.IntegerField()
    total_units = models.IntegerField()

    def __str__(self):
        return f"{self.order_number}"

                                                
class Order(models.Model):
    barcode = models.CharField(max_length=30)
    order_number = models.IntegerField()
    lisa_number = models.IntegerField()
    box_number = models.CharField(max_length=20)
    ean_sku = models.CharField(max_length=30)
    sku = models.CharField(max_length=30)
    quantity_Shipped = models.IntegerField()
    quantity_ordered = models.IntegerField()
    weight = models.FloatField()
    volume = models.FloatField()
    ean_store = models.CharField(max_length=30)
    customer_code = models.IntegerField()
    customer_nit = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=30)
    address_delivery = models.CharField(max_length=50)
    city_delivery = models.CharField(max_length=30)
    ean_sbd = models.CharField(max_length=20)
    nit_sbd = models.CharField(max_length=20)
    sbd_address = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=30)
    order_confirmation = models.CharField(max_length=20)
    order_date_lisa = models.DateField()
    order_closing_date = models.DateField()
    ean_customer = models.CharField(max_length=20)
    customer_destination = models.CharField(max_length=20)
    total_weight = models.FloatField()
    total_volume = models.FloatField()
    order_opening_date_lds = models.DateField()
    order_closing_date_lds = models.DateField()
    status_order = models.CharField(max_length=20)
    number_of_prints = models.IntegerField()
    printing_format = models.TextField()
    printer_user = models.ForeignKey(UserPrinter, on_delete=models.CASCADE)
    remision_number = models.IntegerField()
    
    def __str__(self):
        return f"{self.order_number}"
