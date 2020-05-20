# Generated by Django 2.2.5 on 2020-05-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_restaurante_slug_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='provincia',
            field=models.CharField(default='Alicante', max_length=50, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='telefono',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]
