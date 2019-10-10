import io
import json

from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import WatsonApiException
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource

watson_configuration_filename = '/Users/benn/.bluemix/config.json'
watson_stt_apikey_filename = '/Users/benn/.bluemix/stt_credentials.json'
url = 'https://stream.watsonplatform.net/speech-to-text/api'
audio_fn = 'data/emergency-broadcast-system-test-1983.mp3' 
audio_fn_type = 'audio/mp3'
audio_fn_model = 'en-US_BroadbandModel'

# Presume the configuration file is loaded as result of an `ibmcloud login` operation
with open(watson_configuration_filename, 'r') as watson_config_file:
    watson_config = json.loads(watson_config_file.read())

# https://console.bluemix.net/dashboard/apps -> Create Resource -> Speech to Text -> Create
with open(watson_stt_apikey_filename, 'r') as stt_apikey_file:
    stt_cred = json.loads(stt_apikey_file.read())

stt = SpeechToTextV1(iam_apikey=stt_cred['apikey'], url=url)

stt.set_detailed_response(True)
stt.set_default_headers({'x-watson-learning-opt-out': 'true'})


class WatsonSTTCallback(RecognizeCallback):
    def on_data(self, data):
        print('on_data callback:')
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('on_error callback: {}'.format(error))

    def on_inactivity_timeout(self, inactivity_timeout):
        print('on_inactivity_timeout callback: {}'.format(inactivity_timeout))

try:
    with open(audio_fn, 'rb') as audio_file:
        audio_fll = io.BytesIO(audio_file.read())
        audio_src = AudioSource(audio_fll)

        stt_callback = WatsonSTTCallback()
        response = stt.recognize_using_websocket(audio=audio_src, content_type=audio_fn_type,
                recognize_callback=stt_callback,
                model=audio_fn_model)

        # Experimentally, response is None and the above call blocks until it's complete.
        # The on_data callback is called once with the result.
        if response:
            try:
                print('Status Code: ' + str(response.get_status_code()))
                print('Result: ' + json.dumps(response.get_result(), indent=2))
                print('Headers: ', response.get_headers())
            except Exception as ex:
                print('Exception: ' + str(ex))
        else:
            print('Response is None')
except WatsonApiException as ex:
    print('Method failed: ' + str(ex.code) + ': ' + ex.message)
