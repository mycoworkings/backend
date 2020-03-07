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




#### TEST ####

@parser_classes((JSONParser,))
@api_view(['POST','GET'])
@csrf_exempt
def Test(request):
    
    if request.method == 'GET':

        return Response({
  "coworkings": [
    {
      "description": {
        "name": "My coworking Piscina de Billetes",
        "openingDate": "datetime",
        "description": "El yate ya esta amarrado"
      },
      "location": {
        "provinceCode": 21,
        "munipalityCode": 35,
        "streetCode": 343,
        "postalCode": "08018",
        "latitude": 3.3213,
        "longitude": 2.3213
      },
      "contact": {
        "phoneNumber": "658063523",
        "email": "unemail@gmail.com",
        "webURL": "http://www.myweb.com",
        "socialMedia": {
          "facebook": {
            "hasFacebook": True,
            "facebookUrl": "http://www.facebook.com/algo"
          },
          "instagram": {
            "hasInstagram": True,
            "instagramUrl": "http://www.instagram.com/algo"
          },
          "twitter": {
            "hasTwitter": False,
            "twitterUrl": None
          },
          "linkedin": {
            "hasLinkedin": True,
            "linkedinUrl": "http://www.linkedin.com/algo"
          }
        }
      },
      "services": {
        "basicServices": {
          "hasWifi": True,
          "hasClimatization": True,
          "is24h": False,
          "hasCoffe": True
        },
        "communityServices": {
          "hasEvents": True,
          "hasWorkshops": True,
          "hasAccelerator": True,
          "hasIncubator": False
        },
        "relaxServices": {
          "hasTerrace": True,
          "hasChillOutArea": False
        }
      },
      "meetingRooms": [
        {
          "name": "Meeting Room A",
          "capacity": 20,
          "pricePerDay": 100,
          "pricePerWeek": "null",
          "pricePerMonth": "null",
          "description": "A nice meeting room",
          "openingHours": "datetime"
        },
        {
          "name": "Meeting Room A",
          "capacity": 12,
          "pricePerDay": "null",
          "pricePerWeek": "null",
          "pricePerMonth": 900,
          "description": "Nicest meeting room",
          "openingHours": "datetime"
        }
      ],
      "desks": [
        {
          "deskTypeName": "Desk type A",
          "totalPlaces": 100,
          "pricePerDay": 40,
          "pricePerWeek": "null",
          "pricePerMonth": "null",
          "description": "A beautiful desk",
          "openingHours": "datetime"
        },
        {
          "deskTypeName": "Desk type B",
          "totalPlaces": 20,
          "pricePerDay": "null",
          "pricePerWeek": "null",
          "pricePerMonth": 300,
          "description": "A more beautiful desk",
          "openingHours": "datetime"
        }
      ],
      "conferenceRooms": [
        {
          "conferenceRoomName": "Conference room A",
          "totalPlaces": 50,
          "pricePerDay": "200",
          "pricePerWeek": "null",
          "pricePerMonth": "null",
          "description": "A beautiful meeting room",
          "openingHours": "datetime"
        },
        {
          "deskTypeName": "Conference room B",
          "totalPlaces": 200,
          "pricePerDay": "null",
          "pricePerWeek": "null",
          "pricePerMonth": 8000,
          "description": "A more beautiful meeting room",
          "openingHours": "datetime"
        }
      ],
      "array": [
        "photo1.png",
        "photo2.png",
        "photo3.png"
      ]
    }
  ]
}, 
            status=200
        )


    if request.method == 'POST':
        
        
        
        return Response({"msg":"post"},status=200)