from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarsListSerializer
from cars.models import Car
from cars.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

    #переопределяем работу
    def post(self,request):
        print(request.data)
        print(request.POST)
        return Response({1:123})


class CarListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser,)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    #authentication_classes = (TokenAuthentication, SessionAuthentication) 
    #можно объявить разные методы аутентификации один раз сразу для всех
    #в settings.py
    permission_classes = (IsOwnerOrReadOnly,)