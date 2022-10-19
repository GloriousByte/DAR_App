from django.db import models


# Create your models here.

class Citizen(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    CATEGORY = (
        ('A Type', 'B Type'),
        ('C Type', 'D Type'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Receipt(models.Model):
    STATUS = (
        ('Issued', 'Issued'),
        ('Pending', 'Pending'),
        ('No Payment', 'No Payment'),
    )

    citizen = models.ForeignKey(Citizen, null=True, on_delete=models.SET_NULL)
    property = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.property.name
