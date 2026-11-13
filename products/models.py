from django.db import models

class Product(models.Model):
    id = models.BigIntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200, blank=False)
    brand = models.CharField(max_length=200, blank=False)
    volume = models.IntegerField(blank=False)
    price = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False)
    create_at = models.DateField(auto_now=True)
    updated_at = models.DateField()

    def __str__(self): #This is important to be always implemented, because the the object representation used by django 
        return f"{self.name} - {self.brand}"
