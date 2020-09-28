import json
import boto3

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table("formTable")
    a = table.get_item(Key={'ip': 'home'})
    #ip =1# table.get_item(Key={'IP': 1})
    return {
            'statusCode': 200,
            'body':  json.dumps(ip["Item"]["IP"])
        }
