from rest_framework import serializers
from .models import Component, Vehicle, Repair, Revenue

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    vehicle_number = serializers.CharField(source='vehicle_id')
    issue_description = serializers.CharField()
    class Meta:
        model = Vehicle
        fields = ['id','vehicle_number', 'issue_description', 'created_at']

class RepairSerializer(serializers.ModelSerializer):
    vehicle = serializers.SerializerMethodField()
    components = serializers.SerializerMethodField()

    class Meta:
        model = Repair
        fields = ['vehicle', 'components', 'total_cost', 'created_at']

    def get_vehicle(self, obj):
        return {
            "vehicle_number": obj.vehicle.vehicle_id,
            "issue_description": obj.vehicle.issue_description,
        }

    def get_components(self, obj):
        return [component.name for component in obj.components.all()]

    def create(self, validated_data):
        components_data = validated_data.pop('components', [])
        repair_instance = Repair.objects.create(**validated_data)
        repair_instance.components.set(components_data)
        repair_instance.total_cost = sum(component.repair_price for component in repair_instance.components.all())
        repair_instance.save()
        if repair_instance.total_cost > 0:
            revenue = Revenue(
                date=repair_instance.created_at.date(), 
                revenue_amount=repair_instance.total_cost 
            )
            revenue.save()

        return repair_instance
class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'
