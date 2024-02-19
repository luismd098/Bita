from django.urls import re_path
from BitaApi import views

urlpatterns = [
    re_path(r'^login$',views.loginApi),    
    re_path(r'^login/([0-9]+)$',views.loginApi),   
    re_path(r'^areas$',views.areasApi),    
    re_path(r'^areas/([0-9]+)$',views.areasApi),   
    re_path(r'^bitacoras$',views.bitacorasApi),    
    re_path(r'^bitacoras/([0-9]+)$',views.bitacorasApi),   
    re_path(r'^estatusReportes$',views.estatusReportesApi),    
    re_path(r'^estatusReportes/([0-9]+)$',views.estatusReportesApi),   
    re_path(r'^licencias$',views.licenciasApi),    
    re_path(r'^licencias/([0-9]+)$',views.licenciasApi),     
    re_path(r'^licenciasBitacoras$',views.licenciasBitacorasApi),    
    re_path(r'^licenciasBitacoras/([0-9]+)$',views.licenciasBitacorasApi),   
    re_path(r'^reportes$',views.reportesApi),    
    re_path(r'^reportes/([0-9]+)$',views.reportesApi),   
]
