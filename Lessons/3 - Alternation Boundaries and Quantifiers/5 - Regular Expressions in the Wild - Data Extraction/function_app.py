import os
import re
import azure.functions as func

def main(myblob: func.InputStream, name: str, outputblob: func.Out[str]):
    # Read the blob content
    content = myblob.read().decode('utf-8')

    # Extract phone numbers
    phone = re.findall(r'\(\d{3}\) \d{3}-\d{4}', content)

    # Convert list of phone numbers
    phone_string = "\n".join(phone)

    # Output to another blob
    outputblob.set(phone_string)
