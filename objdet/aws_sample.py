import boto3

if __name__ == "__main__":

    imageFile='./data/450px-Broadway_and_Times_Square_by_night.jpg'
    region = 'us-east-1'

    client = boto3.client('rekognition', region_name=region)
   
    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + imageFile)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    print('Done...')
