from django.db import models


class Family(models.Model):
    """ 科 """
    name = models.CharField('名前', max_length=50)


class Species(models.Model):
    """ 種 """
    family = models.ForeignKey('fk_app.Family', on_delete=models.CASCADE)
    name = models.CharField('名前', max_length=50)


class Cultivars(models.Model):
    """ 品種 """
    species = models.ForeignKey('fk_app.Species', on_delete=models.CASCADE)
    name = models.CharField('名前', max_length=50)
