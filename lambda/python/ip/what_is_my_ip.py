import json

def lambda_handler(event, context):
    ip =  event["requestContext"]["identity"]["sourceIp"]
    return {
            'statusCode': 200,
            'body': json.dumps(ip)
        }
