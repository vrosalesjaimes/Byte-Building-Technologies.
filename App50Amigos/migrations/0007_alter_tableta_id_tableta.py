# Generated by Django 4.1.6 on 2023-06-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App50Amigos', '0006_platillo_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableta',
            name='id_Tableta',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
