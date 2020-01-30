from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from ApiRest.utils import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    


@parser_classes((JSONParser,))
@api_view(['POST','GET'])
@csrf_exempt
def changequota_user(request):
    if request.method == 'GET':

        return Response({
                "user_name":"ejemplo_user",
                "new_quota":"100",
                "APIKEY":"yourapikey",
                
            }, 
            status=200
        )


    if request.method == 'POST':
        
        try:
            mysql = MySql ()
        except Exception as e:
            return Response({"msg":"no se puede conectar","Error":str(e)},status=200)
        domain_name = request.data['user_name']
        quota = request.data['new_quota']

        #pendiente de validaciones
        
        return Response({"msg":quota},status=200)


@parser_classes((JSONParser,))
@api_view(['POST','GET'])
@csrf_exempt
def Register_user(request):
    
    if request.method == 'GET':

        return Response({
                "Nombre_Coworking":"piscina_de_billetes",
                "Descripcion":"nininini",
                "fotos":"la foto",
                "Municipio":"tabarnia",
                "provincia":"narnaia",
                "direccion":"calle falsa",
                "CP":"Tumadre",
                "telefono":"55555555",
                "Email":"pollaroid@dejatellevar.com",
                "web":"puntx.com",
                "redes_sociales":"puntx.com",
                
                
            }, 
            status=200
        )


    if request.method == 'POST':
        
        try:
            mysql = MySql ()
        except Exception as e:
            return Response({"msg":"no se puede conectar","Error":str(e)},status=200)
        try:
            Nombre_Coworking = request.data['Nombre_Coworking']
        except:
            return Response({"msg":"necesitas un nombre"},status=400)
        
        Descripcion = request.data.get('Descripcion', None)
        fotos = request.data.get('fotos', None)
        Municipio = request.data.get('Municipio', None)
        provincia = request.data.get('provincia', None)
        direccion = request.data.get('direccion', None)
        CP = request.data.get('CP', None)
        telefono = request.data.get('telefono', None)
        Email = request.data.get('Email', None)
        web = request.data.get('web', None)
        redes_sociales = request.data.get('redes_sociales', None)
        

        #pendiente de validaciones
        
        return Response({"msg":Descripcion},status=200)