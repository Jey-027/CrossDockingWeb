from django.db import models

class LisaFile(models.Model):
    order_number = models.IntegerField(primary_key=True)
    box_number = models.CharField(max_length=20)
    lisa_number = models.IntegerField()
    ean_sku = models.CharField(max_length=20)
    sku = models.CharField(max_length=30)
    quantity_inventoried = models.IntegerField()
    quantity_ordered = models.IntegerField()
    weight = models.FloatField()
    volume = models.FloatField()
    ean_store = models.CharField(max_length=20, null=True, blank=True)
    customer_code = models.IntegerField()
    customer_nit = models.BigIntegerField()
    customer_name = models.CharField(max_length=30)
    address_delivery = models.CharField(max_length=40)
    city_delivery = models.CharField(max_length=30)
    ean_sbd = models.CharField(max_length=20)
    sbd_nit = models.CharField(max_length=20)
    sbd_address = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=30)
    order_status = models.CharField(max_length=20)
    order_date_lisa = models.DateTimeField()
    order_closing_date = models.DateTimeField()

    def __str__(self):
        return f"{self.order_number}" 


class CenFile(models.Model):
    oc_number = models.IntegerField()
    oc_date = models.DateField()
    order_number = models.IntegerField(primary_key=True)
    ean_code_1 = models.CharField(max_length=15)
    ean_code_2 = models.CharField(max_length=15)
    ean_store = models.CharField(max_length=15)
    ean_sku = models.CharField(max_length=15)
    quantity = models.FloatField()
    field_1 = models.FloatField()
    field_2 = models.FloatField()
    field_3 = models.FloatField()
    field_4 = models.FloatField()
    field_5 = models.FloatField()
    field_6 = models.CharField(max_length=5)
    field_7 = models.CharField(max_length=5)
    field_8 = models.CharField(max_length=5)
    field_9 = models.CharField(max_length=5)
    due_date = models.DateField()
    channel = models.CharField(max_length=5)
    cross_docking = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.order_number}"
