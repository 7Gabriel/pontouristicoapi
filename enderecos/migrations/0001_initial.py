# Generated by Django 3.0.3 on 2020-02-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.TextField(max_length=150)),
                ('linha1', models.TextField(max_length=150)),
            ],
        ),
    ]