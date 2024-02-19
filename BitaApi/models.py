from django.db import models

# Create your models here.

class Usuario(models.Model):
    UsuarioId = models.AutoField(primary_key=True)
    Usuario = models.CharField(max_length=30, unique = True)
    Password = models.CharField(max_length=30)
    Nombre = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    FCreacion = models.DateTimeField(auto_now_add  = True)
    Activo = models.BooleanField(default = True)
    Privilegios = models.ForeignKey(
        "Privilegio", related_name='Privilegios', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.Usuario = self.Usuario.lower()            
        return super(Usuario, self).save(*args, **kwargs)
    
class Privilegio(models.Model):
    PrivilegioId = models.AutoField(primary_key=True)    
    Nombre = models.CharField(max_length = 50)
    Eliminar = models.BooleanField(default = True)
    Agregar = models.BooleanField(default = True)
    Editar = models.BooleanField(default = True)
    FechaCreacion = models.DateTimeField(auto_now_add  = True)
    Activo = models.BooleanField(default = True)
    
class Bitacora(models.Model):
    BitacoraId = models.AutoField(primary_key=True)    
    Nombre = models.CharField(max_length = 100)
    NumeroEquipo = models.IntegerField()
    Modelo = models.CharField(max_length = 50)
    Version = models.CharField(max_length = 50)
    FechaCreacion = models.DateTimeField(auto_now_add  = True)
    Activo = models.BooleanField(default = True)
    Area = models.ForeignKey(
        "Area", on_delete=models.CASCADE)
    
class Area(models.Model):
    AreaId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length = 100)  
    TipoArea = models.CharField(max_length = 100)  
    
class EstatusReporte(models.Model):
    EstatusReporteId = models.AutoField(primary_key=True)
    Color = models.CharField(max_length = 20)
    DescripcionCorta = models.CharField(max_length = 50)
    Descripcion = models.CharField(max_length = 200)
    
class Licencia(models.Model):
    LicenciaId = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length = 200)    
    FechaCreacion = models.DateTimeField(auto_now_add  = True)
    Activo = models.BooleanField(default = True)
    
class RelBitacoraLicencia(models.Model):
    RelId = models.AutoField(primary_key=True)
    Activo = models.BooleanField(default = True)
    FechaCreacion = models.DateTimeField(auto_now_add  = True)
    FechaActualizacion = models.DateTimeField(auto_now_add  = True)
    Licencias = models.ForeignKey(
        "Licencia", on_delete=models.DO_NOTHING)
    Bitacoras = models.ForeignKey(
        "Bitacora", on_delete=models.DO_NOTHING)
    
class Reporte(models.Model):
    ReporteId = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length = 1000)    
    FechaCreacion = models.DateTimeField(auto_now_add  = True)
    Activo = models.BooleanField(default = True)
    Bitacoras = models.ForeignKey(
        "Bitacora", on_delete=models.CASCADE)
    EstatusReportes = models.ForeignKey(
        "EstatusReporte", on_delete=models.CASCADE)
    
    

    # reportes
    
    # apartados de laboratorio
    # apartado para los equipos de admnistrativo
    # los equipos se dan de alta desde la aplicacion
    # solo los de laboratario
    
    # bitacora:
    # (administrativos) por numero de departamento
    # (ctc) por numero de equipo
    # Color naranja por default
    # Solo el administrador elimina las Bitacoras
    
    
    # reportes:
    # fecha
    # nombre equipo
    # estatus (color)
    
    
    #usuario normal
    #agregar
    #visualizar
    
    
    
    
    
    