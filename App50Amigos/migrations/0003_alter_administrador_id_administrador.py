# Generated by Django 4.1.6 on 2023-05-31 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App50Amigos', '0002_rename_id_adminustrador_menu_id_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='id_Administrador',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
