import requests
import json

url = 'http://127.0.0.1:8080/predict/'
data = {'sepal_length': 7.0, 'sepal_width': 6.2, 'petal_length': 5,'petal_width': 0.5}
r =requests.post(url, json = data)
print(r.json())
