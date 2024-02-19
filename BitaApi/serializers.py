from rest_framework import serializers
from BitaApi.models import Usuario,Privilegio,Area,Bitacora,EstatusReporte,Licencia,RelBitacoraLicencia,Reporte


class PrivilegioSerializer(serializers.ModelSerializer):
    class Meta:
            model = Privilegio
            fields = '__all__'
            
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
            model = Usuario
            fields = ('UsuarioId','Usuario','Password','Nombre','Apellidos','Activo','Privilegios')
    def to_representation(self, instance):
        self.fields['Privilegios'] =  PrivilegioSerializer(read_only=True)
        return super(UsuarioSerializer, self).to_representation(instance)
    
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Area
            fields = '__all__'
            
class BitacoraSerializer(serializers.ModelSerializer):
    class Meta:
            model = Bitacora
            fields = ('BitacoraId','Nombre','NumeroEquipo','Modelo','Version','Activo','Area')
            
    def to_representation(self, instance):
        self.fields['Area'] =  AreaSerializer(read_only=True)
        return super(BitacoraSerializer, self).to_representation(instance)
    
class EstatusReporteSerializer(serializers.ModelSerializer):
    class Meta:
            model = EstatusReporte
            fields = '__all__'

class LicenciaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Licencia
            fields = '__all__'
            
class RelBitacoraLicenciaSerializer(serializers.ModelSerializer):
    class Meta:
            model = RelBitacoraLicencia
            fields = ("RelId","Activo","FechaCreacion","FechaActualizacion","Licencias","Bitacoras")
    
    def to_representation(self, instance):
        self.fields['Licencias'] =  LicenciaSerializer(read_only=True)
        self.fields['Bitacoras'] =  BitacoraSerializer(read_only=True)
        return super(RelBitacoraLicenciaSerializer, self).to_representation(instance)
    
class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
            model = Reporte
            fields = ("ReporteId","Descripcion","FechaCreacion","Activo","EstatusReportes","Bitacoras")
    
    def to_representation(self, instance):
        self.fields['EstatusReportes'] =  EstatusReporteSerializer(read_only=True)
        self.fields['Bitacoras'] =  BitacoraSerializer(read_only=True)
        return super(ReporteSerializer, self).to_representation(instance)