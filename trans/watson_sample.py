import json

from watson_developer_cloud import LanguageTranslatorV3


apikey_fn = '/Users/benn/.bluemix/translate_credentials.json'
input_fn = './input.txt'

# https://console.bluemix.net/dashboard/apps -> Create Resource -> * -> Create
with open(apikey_fn, 'r') as apikey_file:
    api_cred = json.loads(apikey_file.read())

with open(input_fn, 'r') as input_file:
    input_txt = input_file.read()

translate = LanguageTranslatorV3(version='2018-05-01', iam_apikey=api_cred['apikey'], url='https://gateway.watsonplatform.net/language-translator/api')

translate.set_detailed_response(True)
translate.set_default_headers({'x-watson-learning-opt-out': 'true'})

result = translate.translate(text=input_txt, model_id='en-es').get_result()

print(json.dumps(result, indent=2, ensure_ascii=False))
