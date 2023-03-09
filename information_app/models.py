from django.db import models


class UserPrinter(models.Model):
    user = models.CharField(max_length=20, primary_key=True)
    user_terminal = models.CharField(max_length=20)
    ip_printer = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user}"


class Product(models.Model):
    sku = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=100)
    ean_sku = models.CharField(max_length=15)
    weight = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return f"{self.sku}"


class OrderStatus(models.Model):
    status_code = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=20)
    status_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.status_name}"


class Store(models.Model):
    ean = models.CharField(max_length=30, primary_key=True)
    store_code = models.CharField(max_length=10)
    store_name = models.CharField(max_length=50)
    priority = models.IntegerField()
    address = models.CharField(max_length=100)
    company = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    store_advisor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.store_name}"


class parameters(models.Model):
     name = models.CharField(max_length=100)
     value = models.CharField(max_length=100)

     def __str__(self):
         return f"{self.name}"
