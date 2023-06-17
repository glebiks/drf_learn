from rest_framework import serializers
from cars.models import Car

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarsListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    #если наш сервис проксирующий, (принимает запросы от клиента и они 
    # проксируются на другой наш внутренний сервис, то наш сервис является
    # валидацией, синхронизацией и временным хранилищем

    # необязательно передавать только те данные, что есть в модели:
    email = serializers.Serializer(label='3241231', required=False)

    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')

