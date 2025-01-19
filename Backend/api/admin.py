from django.contrib import admin
from .models import Component, Vehicle, Repair, Revenue

admin.site.register(Component)
admin.site.register(Vehicle)
admin.site.register(Repair)
admin.site.register(Revenue)
