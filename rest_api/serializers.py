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
        fields = ['car_id', 'rate']


class CarListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']


class PopularitySerializer:
    rates_number = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']
