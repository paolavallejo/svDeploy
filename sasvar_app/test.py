import requests

API_URL = "https://api-inference.huggingface.co/models/pvallej3/garbage_classifier"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("botella.jpg")
print(output)


# https://huggingface.co/pvallej3/garbage_classifier
# https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification
