import requests
import json
import os
import uuid
from io import BytesIO

apikey_fn = '/Users/benn/.azure/sai_trans_test_keys.json'
input_fn = './input.txt'

with open(apikey_fn, 'r') as apikey_file:
    api_cred = json.loads(apikey_file.read())

with open(input_fn, 'r') as input_file:
    input_txt = input_file.read()

base_url = 'https://api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'
params = '&to=es'
constructed_url = base_url + path + params

headers = {
        'Ocp-Apim-Subscription-Key': api_cred['key_1'],
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

body = [{
    'text' : input_txt
}]

request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))

