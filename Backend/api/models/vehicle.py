from django.db import models

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True) 
    vehicle_id = models.CharField(max_length=100, unique=True) 
    issue_description = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.vehicle_id

