import requests
import json
import pandas as pd
url = 'http://0.0.0.0:8080/files/'

files = {'file': open('./input.csv', 'rb')}
# The key inside {'file':} need to match the field name file when declare inside the query parameters : async def external_file(file: UploadFile = File(...)) from main.py

res = requests.post(url, files = files)
print(res.json())
