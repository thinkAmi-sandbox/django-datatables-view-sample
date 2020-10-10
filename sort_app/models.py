from django.db import models


class Color(models.Model):
    name = models.CharField('色', max_length=10)


class Apple(models.Model):
    name = models.CharField('品種', max_length=50)
    color = models.ForeignKey('sort_app.Color', on_delete=models.CASCADE)
    breeding = models.CharField('交配', max_length=100)
    season = models.IntegerField('旬')
    born_in_nagano = models.BooleanField('長野県生まれ')

