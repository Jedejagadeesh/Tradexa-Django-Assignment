from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Order {self.id}"


class Box(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    max_weight = models.FloatField()

    def __str__(self):
        return self.name