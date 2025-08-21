def lambda_handler(event, context):
    # Parse text from the request body
    input_text = event.get('queryStringParameters', {}).get('text', '')

    # Sample processing: Convert to uppercase
    result = input_text.upper()

    return {
        'statusCode': 200,
        'body': f'Processed Text: HELLO--HIMANSHU'
    }
