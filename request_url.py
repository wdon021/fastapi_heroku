import requests
import json

url = 'https://rap-dev-opencesus-fastapi.azurewebsites.net/predict/'
data = {'sepal_length': 1.0, 'sepal_width': 1.2, 'petal_length': 1}
r =requests.post(url, json = data)
print(r.json())
