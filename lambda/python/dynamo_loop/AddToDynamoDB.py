import json
import boto3

def lambda_handler(event, context):
    client = boto3.resource('dynamodb') #Inicialize dynamodb
    if event["password"] == "SuperPassword":
        for user in event["data"]:
            context = user["context"]
            table = client.Table(context) #Select Table
            table.put_item(Item={'Number': user["Number"] ,'Name':  user["Name"] , 'Age': user["Age"], 'Tittle': user["Tittle"], 'Info': user["Info"]})
        return {
            'statusCode': 201
        }
    else:
        return {
            'statusCode': 401
        }
