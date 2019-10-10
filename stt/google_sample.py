import io

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def sample_stt():
    # Instantiates a client
    client = speech.SpeechClient()

    # Note: must be 44100 and mono.
    file_name = './stt/data/emergency-broadcast-system-test-1983.mono.wav'

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    result = {
            'transcript': response.results[0].alternatives[0].transcript,
            'confidence': response.results[0].alternatives[0].confidence
        }

    return result
