import boto3
import re
import os

def lambda_handler(event, context):
    username =  event['queryStringParameters']['username']

    pattern = r'^[a-zA-Z][a-zA-Z0-9]{2,15}$'
    if re.match(pattern, username):
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Valid username'})
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid username'})
        }
