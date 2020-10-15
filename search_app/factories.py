import factory

from search_app.models import Color, Apple


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color


class AppleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Apple
