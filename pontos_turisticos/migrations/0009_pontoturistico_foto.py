# Generated by Django 3.0.3 on 2020-02-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0008_auto_20200221_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
