import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('books_table')
    response = table.scan()
    
    # Return the response as JSON using the custom encoder
    return {
        'statusCode': 200,
        'body': response["Items"]
    }
