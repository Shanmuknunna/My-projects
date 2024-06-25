import json
import boto3
from botocore.exceptions import ClientError
import requests
import os

def lambda_handler(event, context):
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    # Your S3 bucket name
    bucket_name = 'json-load-1'
    # The key (filename) you want to use for the uploaded file
    key = 'employee_data.json'
    
    # Check if the event is a list (direct JSON data)
    if isinstance(event, list):
        data = event
    else:
        try:
            # If the payload is provided via Lambda event (assume it's a dict with 'body')
            data = event.get('body', None)
            
            # If the body is a JSON string, parse it
            if isinstance(data, str):
                data = json.loads(data)
            elif data is None:
                # If no body is found
                return {
                    'statusCode': 400,
                    'body': json.dumps({'message': 'Request body is empty', 'File_status': 'file is not uploaded'})
                }
                
        except json.JSONDecodeError as e:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': f"Error parsing JSON: {e}", 'File_status': 'file is not uploaded'})
            }
    
    # Convert the JSON data to string
    json_data = json.dumps(data)
    
    try:
        # Upload the JSON file to S3
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=json_data)
        file_status = 'File uploaded successfully'
        
        # Transfer the file to Salesforce
        transfer_status = transfer_to_salesforce(s3_client, bucket_name, key)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'File_status': file_status, 'Salesforce_transfer_status': transfer_status})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f"Error uploading file: {e}", 'File_status': 'file is not uploaded'})
        }

def transfer_to_salesforce(s3_client, bucket_name, key):
    try:
        # Get the file from S3
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
        file_content = s3_object['Body'].read().decode('utf-8')
        
        # Salesforce credentials (ensure these are set as environment variables)
        salesforce_url = os.environ['SALESFORCE_URL']
        salesforce_token = os.environ['SALESFORCE_TOKEN']
        
        # Make a POST request to Salesforce
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {salesforce_token}'
        }
        response = requests.post(salesforce_url, headers=headers, data=file_content)
        
        if response.status_code == 200:
            return 'File transferred to Salesforce successfully'
        else:
            return f'Failed to transfer file to Salesforce: {response.text}'
    except ClientError as e:
        return f'Error fetching file from S3: {e}'
    except requests.RequestException as e:
        return f'Error sending file to Salesforce: {e}'
    
print("Thank You")
