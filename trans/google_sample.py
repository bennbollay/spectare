import os
import io

# Imports the Google Cloud client library
from google.cloud import translate

def sample_translate():
    input_fn = './trans/input.txt'
    target_lang = 'es'

    with open(input_fn, 'r') as input_file:
        input_txt = input_file.read()

    # Instantiates a client
    translate_client = translate.Client()

    # Translates some text into Spanish
    return translate_client.translate(input_txt, target_language=target_lang)
