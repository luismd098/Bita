from django.shortcuts import render
# from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

from BitaApi.models import Usuario,Reporte,Bitacora,RelBitacoraLicencia,Area,EstatusReporte,Licencia

from BitaApi.serializers import UsuarioSerializer,AreaSerializer,BitacoraSerializer,EstatusReporteSerializer,LicenciaSerializer,RelBitacoraLicenciaSerializer,ReporteSerializer

from  BitaApi.utilities.cifrado import AESCipher

# Create your views here.

@csrf_exempt
def loginApi(request,id=0):
    try: 
        if request.method == 'POST':
            data = JSONParser().parse(request)
            cipher = AESCipher()
            
            user = data['user']
            password = data['password']
            
            user = user.lower()
            
            if not Usuario.objects.filter(Usuario = user).exists():
                return JsonResponse({'Msg':'El usuario no existe, favor de validar.','Status':1},safe=False)
            
            user_data = Usuario.objects.get(Usuario = user)
            
            if user_data.Activo == False:
                return JsonResponse({'Msg':'El usuario se encuentra dado de baja.','Status':1},safe=False)
                        
            if not cipher.validate(password,user_data.Password):
                return JsonResponse({'Msg':'La contraseña ingresada es incorrecta, favor de validar.','Status':1},safe=False)
                
            user_serializer = UsuarioSerializer(user_data)
            json_data = user_serializer.data     
            json_data['Status'] = 0                 
            json_data['Msg'] = ''                 
            
            return JsonResponse(json_data,safe=False)                
    except:
        return JsonResponse({'Msg':'Algo salio mal, por favor comunicate con el administrador.','Status':1},safe=False)
    

@csrf_exempt
def areasApi(request,id=0):
    try: 
        if request.method == 'GET':
            bitacoras = Area.objects.all()
            area_serializer = AreaSerializer(bitacoras, many = True)  
            return JsonResponse(area_serializer.data,safe=False)
        
        elif request.method == 'POST':
            area_data = JSONParser().parse(request)
            area_serializer = AreaSerializer(data=area_data)
            if area_serializer.is_valid():
                area_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al agregar el registro.'},safe=False)
        
        elif request.method == 'PUT':
            area_data = JSONParser().parse(request)
            area_id = area_data['AreaId']
            if not Area.objects.filter(AreaId = area_id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)
            
            area = Area.objects.get(AreaId = area_id)
            area_serializer = AreaSerializer(area,data = area_data)
            if area_serializer.is_valid():
                area_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al actualizar el registro.'},safe=False)
        
        elif request.method == 'DELETE':
            if not Area.objects.filter(AreaId = id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)          
            
            area = Area.objects.get(AreaId = id)
            area.delete()
            return JsonResponse({'Status':0,'Msg':''},safe=False)
    except:
        return JsonResponse({'Msg':'Algo salio mal, por favor comunicate con el administrador.','Status':1},safe=False)
        
@csrf_exempt
def bitacorasApi(request,id=0):
    try: 
        if request.method == 'GET':
            bitacoras = Bitacora.objects.all()
            bitacora_serializer = BitacoraSerializer(bitacoras, many = True)  
            return JsonResponse(bitacora_serializer.data,safe=False)
        
        elif request.method == 'POST':
            bitacora_data = JSONParser().parse(request)
            print(bitacora_data)
            bitacora_serializer = BitacoraSerializer(data=bitacora_data)
            if bitacora_serializer.is_valid():
                bitacora_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al agregar el registro.'},safe=False)
        
        elif request.method == 'PUT':
            bitacora_data = JSONParser().parse(request)
            bitacora_id = bitacora_data['BitacoraId']
            if not Bitacora.objects.filter(BitacoraId = bitacora_id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)
            
            bitacora = Bitacora.objects.get(BitacoraId = bitacora_id)
            bitacora_serializer = BitacoraSerializer(bitacora,data = bitacora_data)
            print(bitacora_serializer)
            if bitacora_serializer.is_valid():
                bitacora_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al actualizar el registro.'},safe=False)
        
        elif request.method == 'DELETE':
            if not Bitacora.objects.filter(BitacoraId = id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)          
            
            bitacora = Bitacora.objects.get(BitacoraId = id)
            bitacora.delete()
            return JsonResponse({'Status':0,'Msg':''},safe=False)
    except:
        return JsonResponse({'Msg':'Algo salio mal, por favor comunicate con el administrador.','Status':1},safe=False)
            
@csrf_exempt
def estatusReportesApi(request,id=0):
    try: 
        if request.method == 'GET':
            estatus_reportes = EstatusReporte.objects.all()
            estatus_reportes_serializer = EstatusReporteSerializer(estatus_reportes, many = True)  
            return JsonResponse(estatus_reportes_serializer.data,safe=False)
        
        elif request.method == 'POST':
            estatus_rep_data = JSONParser().parse(request)
            estatus_reportes_serializer = EstatusReporteSerializer(data=estatus_rep_data)
            if estatus_reportes_serializer.is_valid():
                estatus_reportes_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al agregar el registro.'},safe=False)
        
        elif request.method == 'PUT':
            estatus_rep_data = JSONParser().parse(request)
            estatus_rep_id = estatus_rep_data['EstatusReporteId']
            if not EstatusReporte.objects.filter(EstatusReporteId = estatus_rep_id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)
            
            estatus_rep = EstatusReporte.objects.get(EstatusReporteId = estatus_rep_id)
            estatus_reportes_serializer = EstatusReporteSerializer(estatus_rep,data = estatus_rep_data)
            if estatus_reportes_serializer.is_valid():
                estatus_reportes_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al actualizar el registro.'},safe=False)
        
        elif request.method == 'DELETE':
            if not EstatusReporte.objects.filter(EstatusReporteId = id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)          
            
            estatus_rep = EstatusReporte.objects.get(EstatusReporteId = id)
            estatus_rep.delete()
            return JsonResponse({'Status':0,'Msg':''},safe=False)
    except:
        return JsonResponse({'Msg':'Algo salio mal, por favor comunicate con el administrador.','Status':1},safe=False)
        
@csrf_exempt
def licenciasApi(request,id=0):
    try: 
        if request.method == 'GET':
            licencia = Licencia.objects.all()
            licencia_serializer = LicenciaSerializer(licencia, many = True)  
            return JsonResponse(licencia_serializer.data,safe=False)
        
        elif request.method == 'POST':
            licencia_data = JSONParser().parse(request)
            licencia_serializer = LicenciaSerializer(data=licencia_data)
            if licencia_serializer.is_valid():
                licencia_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al agregar el registro.'},safe=False)
        
        elif request.method == 'PUT':
            licencia_data = JSONParser().parse(request)
            licencia_id = licencia_data['LicenciaId']
            if not Licencia.objects.filter(LicenciaId = licencia_id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)
            
            licencia = Licencia.objects.get(LicenciaId = licencia_id)
            licencia_serializer = LicenciaSerializer(licencia,data = licencia_data)
            if licencia_serializer.is_valid():
                licencia_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al actualizar el registro.'},safe=False)
        
        elif request.method == 'DELETE':
            if not Licencia.objects.filter(LicenciaId = id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)          
            
            licencia = Licencia.objects.get(LicenciaId = id)
            licencia.delete()
            return JsonResponse({'Status':0,'Msg':''},safe=False)
    except:
        return JsonResponse({'Msg':'Algo salio mal, por favor comunicate con el administrador.','Status':1},safe=False)
        
         
@csrf_exempt
def licenciasBitacorasApi(request,id=0):
    try: 
        if request.method == 'GET':
            rel_bl = RelBitacoraLicencia.objects.all()
            rel_bl_serializer = RelBitacoraLicenciaSerializer(rel_bl, many = True)  
            return JsonResponse(rel_bl_serializer.data,safe=False)
        
        elif request.method == 'POST':
            rel_bl_data = JSONParser().parse(request)
            rel_bl_serializer = RelBitacoraLicenciaSerializer(data=rel_bl_data)
            if rel_bl_serializer.is_valid():
                rel_bl_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al agregar el registro.'},safe=False)
        
        elif request.method == 'PUT':
            rel_bl_data = JSONParser().parse(request)
            rel_bl_id = rel_bl_data['RelId']
            if not RelBitacoraLicencia.objects.filter(RelId = rel_bl_id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)
            
            rel_bl = RelBitacoraLicencia.objects.get(RelId = rel_bl_id)
            rel_bl_serializer = RelBitacoraLicenciaSerializer(rel_bl,data = rel_bl_data)
            if rel_bl_serializer.is_valid():
                rel_bl_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al actualizar el registro.'},safe=False)
        
        elif request.method == 'DELETE':
            if not RelBitacoraLicencia.objects.filter(RelId = id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)          
            
            rel_bl = RelBitacoraLicencia.objects.get(RelId = id)
            rel_bl.delete()
            return JsonResponse({'Status':0,'Msg':''},safe=False)
    except:
        return JsonResponse({'Msg':'Algo salio mal, por favor comunicate con el administrador.','Status':1},safe=False)
        
@csrf_exempt
def reportesApi(request,id=0):
    try: 
        if request.method == 'GET':
            reportes = Reporte.objects.all()
            reportes_serializer = ReporteSerializer(reportes, many = True)  
            return JsonResponse(reportes_serializer.data,safe=False)
        
        elif request.method == 'POST':
            reporte_data = JSONParser().parse(request)
            reportes_serializer = ReporteSerializer(data=reporte_data)
            if reportes_serializer.is_valid():
                reportes_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al agregar el registro.'},safe=False)
        
        elif request.method == 'PUT':
            reporte_data = JSONParser().parse(request)
            reporte_id = reporte_data['ReporteId']
            if not Reporte.objects.filter(ReporteId = reporte_id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)
            
            reportes = Reporte.objects.get(ReporteId = reporte_id)
            reportes_serializer = ReporteSerializer(reportes,data = reporte_data)
            if reportes_serializer.is_valid():
                reportes_serializer.save()
                return JsonResponse({'Status':0,'Msg':''},safe=False)
            
            return JsonResponse({'Status':1,'Msg':'Algo salio mal al actualizar el registro.'},safe=False)
        
        elif request.method == 'DELETE':
            if not Reporte.objects.filter(ReporteId = id).exists():
                return JsonResponse({'Status':1,'Msg':'No se encontro el registro.'},safe=False)          
            
            reportes = Reporte.objects.get(ReporteId = id)
            reportes.delete()
            return JsonResponse({'Status':0,'Msg':''},safe=False)
    except:
        return JsonResponse({'Msg':'Algo salio mal, por favor comunicate con el administrador.','Status':1},safe=False)
              