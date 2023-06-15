from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    CAR_BRANDS = (
        (1, 'BMW'),
        (2, 'Mercedes'),
        (3, 'Lada'),
        (4, 'Lamborghini'),
    )
    brand = models.IntegerField(verbose_name='brand', choices=CAR_BRANDS)
    CAR_TYPES = (
        (1, 'sedan'),
        (2, 'hatchback'),
        (3, 'coupe'),
        (4, 'station wagon')
    )
    car_type = models.IntegerField(verbose_name='car_type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)