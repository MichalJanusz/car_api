from rest_framework import serializers
from rest_api.models import Car, Rate


# Create your serializers here

class CarCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['car_id', 'rating']


class CarListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.DecimalField(max_digits=2, decimal_places=1)  # annotate avg_rating=Avg('rates__rate')

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']


class PopularSerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField()  # annotate rates_number=Count('rates__rate') and hope that'll work

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']
