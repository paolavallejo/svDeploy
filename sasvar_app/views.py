from django.shortcuts import render
from django.http import HttpResponse

from .models import Waste
#from .util.clasificador import clasificarMaterial

#JC
from .util.clasificador import send_request

import requests
import urllib.parse

import os
from django.http import JsonResponse


from sasvar import settings

from django.views.decorators.csrf import csrf_exempt
import base64

import json

def bienvenida(request): 
    return render(request, 'bienvenida.html')

def inicio(request): 
    return render(request, 'inicio.html')

def escaneo(request):
    context = {'server_url': 'https://u2f5le55w5.execute-api.us-east-2.amazonaws.com/DummyStage/newdata/fromweb', 
               'apikey': 'Gq5isfVY25aCcyxYDf1xa3BocEMrCLUk2IcmfXaw'} 
    return render(request, 'escaneo.html', context)

def intro_1(request): 
    return render(request, 'intro_1.html')

def intro_6(request): 
    return render(request, 'intro_6.html')

def categorias(request): 
    return render(request, 'categorias.html')

def detalle_reci_q1(request): 
    return render(request, 'detalle_reci_q1.html')

def detalle_reci_2(request): 
    return render(request, 'detalle-reci-2.html')

def detalle_no_aprov(request): 
    return render(request, 'detalle-no-aprov.html')

def detalle_org(request): 
    return render(request, 'detalle-org.html')

def carga(request): 
    return render(request, 'carga.html')

def resultado(request, material): 
    return render(request, 'resultado.html', {'resultado_clasificacion': material})

# Temporalmente en tu vista Django para pruebas
@csrf_exempt
def guardar_imagen(request):
    if request.method == 'POST':
        try:
            image = request.FILES['image']
            residuo = Waste(imagen = image, img_name = request.POST['name'], waste_type = ' ', container_id = 1)
            residuo.save()
            #response = clasificarMaterial('sasvar_app/images/' + image.name).json()[0]['label']
            #residuo.waste_type = response
            #residuo.save()

            #JC
            response = send_request('sasvar_app/images/' + image.name)
            res = json.loads(response)
            #print("response", res['prediction'])
            print("Respuesta modelo: ",res['prediction'])
            residuo.waste_type = res['prediction']
            residuo.save()

            return render(request, 'resultado.html', {'resultado_clasificacion': residuo.waste_type})
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Error al guardar la imagen: ' + str(e)})
