# Generated by Django 4.1.6 on 2023-06-02 10:34

import App50Amigos.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_Administrador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidoP', models.CharField(max_length=200)),
                ('apellidoM', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=0, max_length=3)),
                ('contrasenia', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Encargado_Tableta',
            fields=[
                ('id_Encargado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidoP', models.CharField(max_length=200)),
                ('apellidoM', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=0, max_length=3)),
                ('contrasenia', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_Menu', models.AutoField(primary_key=True, serialize=False)),
                ('id_Admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App50Amigos.administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id_Mesa', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(choices=[('terraza', 'Terraza'), ('jardin', 'Jardin'), ('comedor', 'Comedor'), ('balcon', 'Balcon')], max_length=20)),
                ('contrasen', models.CharField(default=0, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_Orden', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ordenar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App50Amigos.orden')),
            ],
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id_Platillo', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(choices=[('entrada', 'Entrada'), ('plato_fuerte', 'Plato Fuerte'), ('postre', 'Postre'), ('bebida', 'Bebida'), ('helado', 'Helado')], max_length=20)),
                ('nombre', models.CharField(default=0, max_length=20)),
                ('costo', models.IntegerField(default=0, max_length=5)),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=1000)),
                ('id_Administrador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App50Amigos.administrador')),
                ('id_Menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App50Amigos.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('mesa', models.CharField(max_length=150, unique=True)),
                ('ubicacion', models.CharField(max_length=150)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', App50Amigos.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tableta',
            fields=[
                ('id_Tableta', models.AutoField(primary_key=True, serialize=False)),
                ('id_Encargado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App50Amigos.encargado_tableta')),
            ],
        ),
        migrations.CreateModel(
            name='PlatilloEnOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App50Amigos.ordenar')),
                ('platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App50Amigos.platillo')),
            ],
        ),
        migrations.AddField(
            model_name='ordenar',
            name='platillos',
            field=models.ManyToManyField(through='App50Amigos.PlatilloEnOrden', to='App50Amigos.platillo'),
        ),
        migrations.AddField(
            model_name='orden',
            name='id_Tableta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App50Amigos.tableta'),
        ),
        migrations.CreateModel(
            name='Estar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ubicacion', models.CharField(blank=True, max_length=20)),
                ('id_Mesa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App50Amigos.mesa')),
                ('id_Tableta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App50Amigos.tableta')),
            ],
        ),
    ]
