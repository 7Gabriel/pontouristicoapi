# Generated by Django 3.0.3 on 2020-02-21 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0005_pontoturistico_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='endereco',
        ),
    ]
