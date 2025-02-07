from django.db import models

class Product(models.Model): #creating a model class
    name = models.CharField(max_length=100) #adding a name field to the model
    price = models.DecimalField(max_digits=10, decimal_places=2) #adding a price field to the model

    def __str__(self):
        return self.name
