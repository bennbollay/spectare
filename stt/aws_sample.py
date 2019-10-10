import time
import boto3
import request

job_name = "emergency_broadcast_1"
job_uri = "s3://sai-stt/emergency-broadcast-system-test-1983.mp3"
region = 'us-east-1'

transcribe = boto3.client('transcribe', region_name=region)
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp3',
    LanguageCode='en-US'
)

while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)

print(status)
resp = request.get(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
print(resp.json())

