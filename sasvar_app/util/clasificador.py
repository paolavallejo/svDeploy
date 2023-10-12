import os
from django.http import JsonResponse
import requests
from sasvar.settings import MEDIA_ROOT

def clasificarMaterial(file):
    try:
        API_URL = "https://api-inference.huggingface.co/models/pvallej3/garbage_classifier"
        headers = {"Authorization": "Bearer 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"}
        
        file_path = os.path.join(MEDIA_ROOT, file)
        with open(file_path, "rb") as f:
            data = f.read()  
        response = requests.post(API_URL, headers=headers, data=data)
        
        return response
    except Exception as e:
        return e