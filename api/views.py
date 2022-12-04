from rest_framework import status
from .models import Places
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from rest_framework.permissions import IsAdminUser
import random

from .serializers import PlacesSerializer


class AddPlace(APIView):
    def post(self, request, place):
        place = place.lower()
        data = {"name": place}
        serializer = PlacesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPlace(APIView):
    def get(self, request, letter):
        places_with_letter = Places.objects.filter(name__startswith=letter).values_list(
            "name", flat=True
        )
        places = random.choice(places_with_letter)
        return JsonResponse({letter: places})


class IfPlace(APIView):
    def get(self, request, place):
        place_exists = Places.objects.filter(name=place).exists()
        if place_exists:
            return JsonResponse({"result": True})
        else:
            return JsonResponse({"result": False})


class GetList(APIView):
    def get(self, request, letter):
        places = Places.objects.filter(name__startswith=letter).values_list(
            "name", flat=True
        )
        print(list(places))
        return JsonResponse({letter: list(places)})


class PlaceViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
