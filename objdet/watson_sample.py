import json

from watson_developer_cloud import VisualRecognitionV3


apikey_fn = '/Users/benn/.bluemix/visual_recognition_credentials.json'
image_fn = 'data/450px-Broadway_and_Times_Square_by_night.jpg'

# https://console.bluemix.net/dashboard/apps -> Create Resource -> * -> Create
with open(apikey_fn, 'r') as stt_apikey_file:
    api_cred = json.loads(stt_apikey_file.read())

vr = VisualRecognitionV3(version='2018-03-19', iam_apikey=api_cred['apikey'])

vr.set_detailed_response(True)
vr.set_default_headers({'x-watson-learning-opt-out': 'true'})

with open('./data/450px-Broadway_and_Times_Square_by_night.jpg', 'rb') as image_file:
    classes = vr.classify(image_file, classifier_ids=['default']).get_result()
    print(json.dumps(classes, indent=2))
