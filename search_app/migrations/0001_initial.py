# Generated by Django 3.1.2 on 2020-10-11 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='色')),
            ],
        ),
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='品種')),
                ('born_in_nagano', models.BooleanField(verbose_name='長野県生まれ')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_app.color')),
            ],
        ),
    ]
