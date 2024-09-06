import json
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    if 'Records' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('No Records found in event.')
        }

    try:
        
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Retrieve the object from S3
        file_obj = s3.get_object(Bucket=bucket, Key=key)
        file_content = file_obj['Body'].read().decode('utf-8')
        
        # Count the number of words
        word_count = len(file_content.split())
        
        # Publish result to SNS
        sns.publish(
            TopicArn='arn:aws:sns:us-west-2:YOUR_ACCOUNT_ID:WordCountAlarm',
            Message=f"The word count for {key} is {word_count}",
            Subject='Word Count Notification'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully processed {key} with {word_count} words.")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
