from django.urls import path
from .views import *
from .views import home


urlpatterns = [
     path('', main, name='main'),# Ruta principal para la página de inicio
     path('index/', index, name='index'),
     path('contacto/', contacto, name='contacto'),
     path('formulario/', formulario, name='formulario'),
     path('login/', login, name='login'),
     path('error/', error, name='error'),
     path('planes/', planes, name='planes'),
     path('registro/', registro, name='registro'),
     path('perfil/', perfil, name='perfil'),
     path('transporte/', transporte, name='transporte'),
     path('lugares/', lugares, name='lugares'),
     # path('hospital/', hospital, name='hospital'),
     # path('comisaria/', comisaria, name='comisaria'),
     
     
]




 