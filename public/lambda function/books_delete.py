import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('books_table')
    
    # Extract book ID from the path parameters
    book_id = event.get('id')
    
    # Check if book ID is provided
    if not book_id:
        return {
            'statusCode': 400,
            'body': json.dumps('Book ID not provided')
        }
    
    # Delete the book item from the DynamoDB table
    try:
        table.delete_item(Key={'id': book_id})
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error deleting book: {str(e)}')
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps('Book deleted successfully!')
    }
