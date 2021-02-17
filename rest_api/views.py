import requests
from django.db.models import Avg, Count
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_api.models import Car
from rest_api.serializers import CarCreationSerializer, CarListSerializer, RateSerializer, PopularSerializer


class CarsView(APIView):

    def post(self, request, format=None):
        serializer = CarCreationSerializer(data=request.data)

        if serializer.is_valid():
            make = serializer.validated_data['make']
            model = serializer.validated_data['model']

            try:
                Car.objects.get(make__iexact=make, model=model)
                already_exist_err = {'error': 'Resource already exists'}
                return Response(already_exist_err, status=status.HTTP_409_CONFLICT)

            except Car.DoesNotExist:
                vehicle_api_response = requests.get(
                    f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json')
                vehicle_resp_json = vehicle_api_response.json()
                results = vehicle_resp_json['Results']
                api_model = list(filter(lambda car: car['Model_Name'] == model, results))

                if len(api_model) == 0:
                    not_found_err = {'error': 'Resource not found'}
                    return Response(not_found_err, status=status.HTTP_404_NOT_FOUND)

                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        cars = Car.objects.all().annotate(avg_rating=Avg('rates__rating')).order_by('pk')
        serializer = CarListSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteCarView(APIView):

    def delete(self, request, pk, format=None):
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RateView(APIView):

    def post(self, request, format=None):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PopularView(APIView):

    def get(self, request, format=None):
        cars = Car.objects.all().annotate(rates_number=Count('rates__rating')).order_by('-rates_number')
        serializer = PopularSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
