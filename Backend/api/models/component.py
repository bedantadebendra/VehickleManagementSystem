from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=255)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
