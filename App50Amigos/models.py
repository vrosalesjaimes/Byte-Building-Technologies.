from django.db import models

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
    id_menu = models.AutoField(primary_key=True)
    id_Adminustrador = models.ForeignKey(Administrador, on_delete=models.SET_NULL, null=True)

class Platillo(models.Model):
    CATEGORIA = (
        ('entrada', 'Entrada'),
        ('plato_fuerte', 'Plato Fuerte'),
        ('postre', 'Postre'),
        ('helado', 'Helado'),
    )
    id_Platillo = models.AutoField(primary_key=True)
    id_Administrador = models.ForeignKey(Administrador, on_delete=models.SET_NULL, null=True)
    id_Menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA)
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

class Estar(models.Model):
    id_Mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True)
    id_Tableta = models.ForeignKey(Tableta, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        if self.id_Mesa:
            self.ubicacion = self.id_Mesa.ubicacion
        super().save(*args, **kwargs)
