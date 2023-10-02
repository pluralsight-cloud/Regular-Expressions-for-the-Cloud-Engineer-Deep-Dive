const pattern = /^[a-zA-Z][a-zA-Z0-9]{2,15}$/;

exports.handler = async (event) => {
    const username = event.queryStringParameters.username;
    
    if (pattern.test(username)) {
        return {
            statusCode: 200,
            body: JSON.stringify({ message: 'Valid username' })
        };
    } else {
        return {
            statusCode: 400,
            body: JSON.stringify({ message: 'Invalid username' })
        };
    }
};
