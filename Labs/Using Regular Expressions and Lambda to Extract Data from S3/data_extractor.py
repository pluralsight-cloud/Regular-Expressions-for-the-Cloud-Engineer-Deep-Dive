import boto3
import re
import os

s3 = boto3.client('s3')

# Define the output bucket name
OUTPUT_BUCKET = 'BUCKET'

def lambda_handler(event, context):
    # Get the object from the event and extract the necessary information
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Download the object from S3
    response = s3.get_object(Bucket=input_bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    # Use regex to capture emails from the content
    email = re.findall(r'REGEX', content)

    # Convert the list of emails into a string for saving to S3
    email_string = "\n".join(email)

    # Create a new key for the extracted emails
    new_key = key.rsplit('.', 1)[0] + '_extracted_email.txt'

    # Upload the extracted emails to the separate S3 output bucket
    s3.put_object(Body=email_string, Bucket=OUTPUT_BUCKET, Key=new_key)

    return {
        'statusCode': 200,
        'body': f'Email addresses extracted and saved to {new_key} in {OUTPUT_BUCKET}!'
    }
