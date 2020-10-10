import factory
from django.contrib.auth.models import User

from sort_app.models import Color, Apple


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color


class AppleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Apple


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'admin'
    password = factory.PostGenerationMethodCall('set_password', 'Passw0rd')
