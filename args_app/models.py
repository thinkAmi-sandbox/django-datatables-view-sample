from django.db import models


class Color(models.Model):
    name = models.CharField('色', max_length=10)


class Apple(models.Model):
    name = models.CharField('品種', max_length=50)
    color = models.ForeignKey('args_app.Color', on_delete=models.CASCADE)
