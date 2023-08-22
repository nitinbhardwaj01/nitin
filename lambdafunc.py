import json
import boto3

client = boto3.client('rekognition')

def lambda_handler(event, context):
    #TODO implement
    
    bucket_name = "facerecognition-img"
    file_name = "Messi.jpg"
    
    response = client.detect_faces(Image={'S3Object':{'Bucket': bucket_name, 'Name': file_name}}, Attributes=['ALL'])
    
    #Process results
    for face in response['FaceDetails']:
        print (json.dumps(face, indent=2))
