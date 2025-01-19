from django.db import models
from .vehicle import Vehicle
from .component import Component
class Repair(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    components = models.ManyToManyField(Component)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repair for {self.vehicle.vehicle_id}"