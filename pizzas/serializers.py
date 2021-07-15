from rest_framework import serializers
from .models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = [
            "pk",
            "name",
            "price",
            "main_topping",
            "size",
            "date_added",
        ]

        extra_kwargs = {
            "date_added": {"required": False},
            "main_topping": {"required": False},

        }

