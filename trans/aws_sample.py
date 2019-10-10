import json
import boto3

input_fn = './input.txt'

with open(input_fn, 'r') as input_file:
    input_txt = input_file.read()

translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
result = translate.translate_text(Text=input_txt, SourceLanguageCode='en', TargetLanguageCode='es')

print(json.dumps(result, indent=2, ensure_ascii=False))
