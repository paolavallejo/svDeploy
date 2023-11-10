import os
import requests
from sasvar.settings import MEDIA_ROOT


#JC
from time import strftime, localtime, time
from sasvar_app.util.Sender import Sender
import cv2 as cv


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
    

# JC
def send_request(file):
    PORT = 8000 # If running on container -> 80
    API = f'https://u2f5le55w5.execute-api.us-east-2.amazonaws.com/DummyStage/newdata/fromweb'
    API_KEY = 'Gq5isfVY25aCcyxYDf1xa3BocEMrCLUk2IcmfXaw'

    date = strftime("%Y-%m-%d_%H:%M:%S", localtime()) # No cambiar formato de la fecha
    
    filepath = os.path.join(MEDIA_ROOT, file)
    im = cv.imread(filepath)
    payload = {
        'frame': im,
        'user': 'test-pao',
    }

    my_sender = Sender(API, API_KEY)
    start = time()
    res = my_sender.send_request(payload)

    if res.status_code == 200:      
        print(f'Elapsed: {round(time()-start, 3)}s')

    return res.text