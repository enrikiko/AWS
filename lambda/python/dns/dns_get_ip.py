import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("table-ip-cortijo")
    ip = table.get_item(Key={'Place': 'cortijo'})
    return {
            'statusCode': 200,
            'body': ip["Item"]["Ip"]
        }
