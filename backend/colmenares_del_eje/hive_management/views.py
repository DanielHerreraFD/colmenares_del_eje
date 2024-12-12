from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from hive_management.serializers import beehive_serializer_input, beehive_serializer_output
from hive_management.models import Beehive

# Create your views here.

class create_hive_view(APIView):
    def post(self, request):
        serializer = beehive_serializer_input(data=request.data)
        serializer.is_valid(raise_exception=True)
        beehive = Beehive.objects.create(**serializer.validated_data)
        serializer = beehive_serializer_output({
            "register_date": beehive.registration_date,
            "location" : beehive.location,
            "open_brood_frames" : beehive.open_brood_frames,
            "capped_brood_frames" : beehive.capped_brood_frames,
            "queen_presence" : beehive.queen_presence,
            "queen_color" : beehive.queen_color,
            "origin" : beehive.origin,
            "food_frames" : beehive.food_frames,
            "observations" : beehive.observations,
            "qr_code" : beehive.qr_code,
            "id_weather_conditions" : beehive.id_weather_conditions,
            "status" : beehive.status
        })
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class edit_hive_view(APIView):
    def patch(self, request, pk=None):
        try:
            beehive = Beehive.objects.get(pk=pk)
        except Beehive.DoesNotExist:
            return Response({"error": "Beehive does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer_input = beehive_serializer_input(beehive, data=request.data, partial=True)
        if serializer_input.is_valid():
            serializer_input.save()
            serializer_output = beehive_serializer_output(beehive)
            return Response(serializer_output.data, status=status.HTTP_200_OK)
        return Response(serializer_input.errors, status=status.HTTP_400_BAD_REQUEST)

class detail_hive_view(APIView):
    def get(self, request, pk=None):
        try:
            beehive = Beehive.objects.get(pk=pk)
        except Beehive.DoesNotExist:
            return Response({"error": "Beehive does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = beehive_serializer_output(beehive)
        return Response(serializer.data, status=status.HTTP_200_OK)

class list_hives_view(APIView):
    def get(self, request):
        beehives = Beehive.objects.all()
        serializer = beehive_serializer_output(beehives, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
