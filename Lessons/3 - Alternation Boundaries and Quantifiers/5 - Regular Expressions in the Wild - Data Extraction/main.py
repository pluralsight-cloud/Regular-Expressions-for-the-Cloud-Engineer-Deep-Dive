import re
from google.cloud import storage

def extract_phone(data, context):
    """Triggered by a change to a Cloud Storage bucket."""
    # Initialize the Cloud Storage client
    client = storage.Client()

    # Get the blob from the triggering event
    bucket_name = data['bucket']
    blob_name = data['name']
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    content = blob.download_as_text()

    # Extract phone
    phone = re.findall(r'\(\d{3}\) \d{3}-\d{4}', content)     email_string = "\n".join(phone)

    # Save the extracted phone to a new blob in the same bucket
    new_blob_name = blob_name + '-extracted.txt'
    new_blob = bucket.blob(new_blob_name)
    new_blob.upload_from_string(email_string)

