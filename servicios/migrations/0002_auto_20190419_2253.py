# Generated by Django 2.1 on 2019-04-20 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_boda',
            name='Descripcion',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='servicio_boda',
            name='Titulo',
            field=models.CharField(max_length=60),
        ),
    ]
