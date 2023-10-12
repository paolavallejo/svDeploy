from django.shortcuts import render
from django.http import HttpResponse

from .models import Waste
from .util.clasificador import clasificarMaterial

import requests
import urllib.parse

import os
from django.http import JsonResponse


from sasvar import settings

from django.views.decorators.csrf import csrf_exempt
import base64


def home(request): 
    return render(request, 'home.html')

def about(request): 
    return HttpResponse('<h1>Welcome to About Page</h1>')

def bienvenida(request): 
    return render(request, 'bienvenida.html')

def inicio(request): 
    return render(request, 'inicio.html')

def escaneo(request): 
    return render(request, 'escaneo.html')

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

def resultado(request): 
    resultado_clasificacion = "PLASTIC"
    return render(request, 'resultado.html', {'resultado_clasificacion': resultado_clasificacion})


"""def guardar_imagen(request):
    if request.method == 'POST':
        # Obtener la imagen capturada desde la solicitud POST
        imagen = request.FILES['imagen']

        # Guardar la imagen en la carpeta de medios
        nombre_archivo = os.path.join('sasvar_app/images', imagen.name)
        with open(os.path.join(settings.MEDIA_ROOT, nombre_archivo), 'wb') as archivo:
            for chunk in imagen.chunks():
                archivo.write(chunk)

        # Devolver una respuesta JSON
        return JsonResponse({'mensaje': 'Imagen guardada con éxito'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
"""  


# Temporalmente en tu vista Django para pruebas
@csrf_exempt
def guardar_imagen(request):
    if request.method == 'POST':
        try:
            image = request.FILES['image']
            residuo = Waste(imagen = image, img_name = request.POST['name'], waste_type = 1, container_id = 1)
            residuo.save()
            response = clasificarMaterial(residuo.imagen.name)
            return JsonResponse({'success': response.json()})
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Error al guardar la imagen: ' + str(e)})


@csrf_exempt
def clasificar(request):
    if request.method == 'POST':
        
        try:
            API_URL = "https://api-inference.huggingface.co/models/pvallej3/garbage_classifier"
            headers = {"Authorization": "Bearer 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"}
            
            pwd = os.path.dirname(__file__)
            file_path = os.path.join(pwd, 'botella.JPG')
            print(pwd)

            with open(file_path, "rb") as f:
                data = f.read()  
            response = requests.post(API_URL, headers=headers, data=data)
            return JsonResponse({'success': response.json()})
        except Exception as e:
            return JsonResponse({'error': 'Error al procesar la imagen: '+ str(e)})

#output = clasificar()
#print(output)


