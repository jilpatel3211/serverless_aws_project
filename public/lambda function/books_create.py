import boto3
import json
import uuid

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('books_table')

    # Extract book data from the event
    book_data = event

    # Ensure that the book_data contains all necessary attributes
   

    # Put the book item into the DynamoDB table
    table.put_item(Item={
        'id':  str(uuid.uuid4()),
        'author': book_data['author'],
        'publisher': book_data['publisher'],
        'title': book_data['title'],
        'year': book_data['year']
    })

    return {
        'statusCode': 201,
        'body': json.dumps('Book created successfully!')
    }
