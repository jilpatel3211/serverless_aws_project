import boto3
import json


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('books_table')

    # Assuming the provided event contains the book data in the specified format
    book_data = event
    
    table.update_item(
        Key={'id':  book_data['id'] },
        UpdateExpression="SET #t = :title, #a = :author, #p = :publisher, #y = :year",
        ExpressionAttributeNames={
            '#t': 'title',
            '#a': 'author',
            '#p': 'publisher',
            '#y': 'year'
        },
        ExpressionAttributeValues={
            ':title': book_data['title'],
            ':author': book_data['author'],
            ':publisher': book_data['publisher'],
            ':year': int(book_data['year'])
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Book updated successfully!')
    }
