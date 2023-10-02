require 'json'

def lambda_handler(event:, context:)
    username = event['queryStringParameters']['username']
    pattern = /^[a-zA-Z][a-zA-Z0-9]{2,15}$/

    if pattern.match?(username)
        {
            statusCode: 200,
            body: JSON.generate(message: 'Valid username')
        }
    else
        {
            statusCode: 400,
            body: JSON.generate(message: 'Invalid username')
        }
    end
end
