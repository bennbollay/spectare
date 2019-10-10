import os
import io
import json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def sample_objdet():
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = './objdet/data/450px-Broadway_and_Times_Square_by_night.jpg'

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Collect the results
    results = { 'labels': {}, 'objects': [], 'faces': []}

    # Performs label detection on the image file
    labels = client.label_detection(image=image).label_annotations
    for label in labels:
        results['labels'][label.description] = {
                'score': label.score,
                'topicality': label.topicality,
                'mid': label.mid
            }


    # Identify objects in the image
    objects = client.object_localization(image=image).localized_object_annotations

    for object_ in objects:
        poly = []
        for vertex in object_.bounding_poly.normalized_vertices:
            poly.append([vertex.x, vertex.y])
        results['objects'].append({
                    'poly': poly,
                    'name': object_.name,
                    'score': object_.score
                })

    # Identify faces in the image
    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    for face in faces:
        poly = []
        for vertex in face.bounding_poly.vertices:
            poly.append([vertex.x, vertex.y])
        results['faces'].append({
                    'poly': poly,
                    'anger': likelihood_name[face.anger_likelihood],
                    'joy': likelihood_name[face.joy_likelihood],
                    'surprise': likelihood_name[face.surprise_likelihood]
                })

    return results
