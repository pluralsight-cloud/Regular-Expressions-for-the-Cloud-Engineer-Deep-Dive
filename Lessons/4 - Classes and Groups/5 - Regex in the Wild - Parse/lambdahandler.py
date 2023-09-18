import re
import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3')

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']

    destination_bucket = 'poe-stories'
    destination_key = 'extracted_headings/' + source_key

    # Retrieve the HTML content from the uploaded file
    response = s3_client.get_object(Bucket=source_bucket, Key=source_key)
    html_content = response['Body'].read().decode('utf-8')

    # Define a regular expression pattern to extract H2 headings
    pattern = r'<h2><a id="[^"]*"></a>([^<]*)<\/h2>'

    # Extract captured headings using the pattern
    captured_headings = [match.group(1) for match in re.finditer(pattern, html_content)]

    # Upload the extracted headings to the destination S3 bucket
    numbered_list = "\n".join([f"{i+1}. {heading}" for i, heading in enumerate(captured_headings)])
    s3_client.put_object(Bucket=destination_bucket, Key=destination_key, Body=numbered_list)

    return {
        'statusCode': 200,
        'body': 'Captured headings extracted and uploaded'
    }
