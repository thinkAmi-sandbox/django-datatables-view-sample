import factory

from fk_app.models import Family, Species, Cultivars


class FamilyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Family


class SpeciesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Species


class CultivarsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cultivars
