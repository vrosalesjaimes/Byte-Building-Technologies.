from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, mesa, ubicacion, **extra_fields):
        values = [mesa, ubicacion]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        mesa = self.normalize_mesa(mesa)
        user = self.model(
            mesa=mesa,
            ubicacion=ubicacion,
            **extra_fields
        )
        user.set_password(ubicacion)
        user.save(using=self._db)
        return user

    def create_user(self, mesa, ubicacion,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mesa, ubicacion, password, **extra_fields)

    def create_superuser(self, mesa, ubicacion,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mesa, ubicacion,password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    mesa = models.CharField(unique=True,max_length=150)
    ubicacion = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'mesa'
    REQUIRED_FIELDS = ['ubicacion']

class Administrador(models.Model):
    id_Administrador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellidoP = models.CharField(max_length=200)
    apellidoM = models.CharField(max_length=200)
    edad = models.IntegerField(default=0, max_length=3)
    contrasenia = models.CharField(max_length=500)

class Encargado_Tableta(models.Model):
    id_Encargado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellidoP = models.CharField(max_length=200)
    apellidoM = models.CharField(max_length=200)
    edad = models.IntegerField(default=0, max_length=3)
    contrasenia = models.CharField(max_length=500)

class Menu(models.Model):
    id_Menu = models.AutoField(primary_key=True)
    id_Admin = models.ForeignKey(Administrador, on_delete=models.SET_NULL, null=True)

class Platillo(models.Model):
    CATEGORIA = (
        ('entrada', 'Entrada'),
        ('plato_fuerte', 'Plato Fuerte'),
        ('postre', 'Postre'),
        ('bebida', 'Bebida'),
        ('helado', 'Helado'),
    )
    id_Platillo = models.AutoField(primary_key=True)
    id_Administrador = models.ForeignKey(Administrador, on_delete=models.SET_NULL, null=True)
    id_Menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA)
    nombre = models.CharField(default = 0, max_length= 20)
    costo = models.IntegerField(default=0, max_length=5)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=1000)

class Tableta(models.Model):
    id_Tableta = models.AutoField(primary_key=True)
    id_Encargado = models.ForeignKey(Encargado_Tableta, on_delete=models.SET_NULL, null=True)

class Orden(models.Model):
    id_Orden = models.AutoField(primary_key=True)
    id_Tableta = models.ForeignKey(Tableta, on_delete=models.SET_NULL, null=True)

class Ordenar(models.Model):
    id_Orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    platillos = models.ManyToManyField(Platillo, through='PlatilloEnOrden')
class PlatilloEnOrden(models.Model):
    orden = models.ForeignKey(Ordenar, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Mesa(models.Model):
    UBICACIONES = (
        ('terraza', 'Terraza'),
        ('jardin', 'Jardin'),
        ('comedor', 'Comedor'),
        ('balcon', 'Balcon'),
    )
    id_Mesa = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=20, choices=UBICACIONES)
    contrasen = models.CharField(default= 0, max_length= 20)
class Estar(models.Model):
    id_Mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True)
    id_Tableta = models.ForeignKey(Tableta, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        if self.id_Mesa:
            self.ubicacion = self.id_Mesa.ubicacion
        super().save(*args, **kwargs)

