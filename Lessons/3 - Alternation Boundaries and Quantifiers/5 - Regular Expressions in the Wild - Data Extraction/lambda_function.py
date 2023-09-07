import boto3
import re
import os

OUTPUT_BUCKET = 'BUCKET_NAME'

def lambda_handler(event, context):
    input_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=input_bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    phone = re.findall(r'\(\d{3}\) \d{3}-\d{4}', content)

    phone_string = "\n".join(phone)

    new_key = key.rsplit('.', 1)[0] + '_extracted_phone.txt'

    s3.put_object(Body=phone_string, Bucket=OUTPUT_BUCKET, Key=new_key)

    return {
        'statusCode': 200,
        'body': f'Phone numbers extracted and saved to {new_key} in {OUTPUT_BUCKET}!'
    }

