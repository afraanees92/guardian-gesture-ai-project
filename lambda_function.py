import json
import boto3
from datetime import datetime

rekognition = boto3.client('rekognition')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:200488542271:EmergencyAlerttopic'


def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        MaxLabels=10
    )

    labels = response['Labels']

    for label in labels:
        print(label['Name'], label['Confidence'])

    emergency_keywords = [
        'Person',
        'Human',
        'Face',
        'Hand',
        'Finger',
        'Gesture',
        'Fire',
        'Smoke',
        'Crowd'
    ]

    for label in labels:

        if label['Name'] in emergency_keywords and label['Confidence'] > 80:

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject='Emergency Alert',
                Message=f"""
Detected: {label['Name']}
Confidence: {label['Confidence']:.2f}%
Image: {key}
Time: {current_time}
"""
            )

    return {
        'statusCode': 200,
        'body': json.dumps('Detection completed')
    }